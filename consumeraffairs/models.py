from django.db import models


class Events(models.Model):
    """
    NOTE: I should have named this Event.

    id = Primary Key
    session_id = user id, browser session id or IP - whichever makes the most sense for "following" a user
    entity_id = "foreign key" linking to a site, API consumer, etc.  I would use an ID vs char for better indexing.
        I would define this in a table so a user could update entities though a UI
        instead of an engineer updating a list of constants in code.
    action_name("name"): What action was performed. QUESTION: Should we make this and action_categories foreign keys
        to another table so 1) a user can update the values though a UI and 2) searching would be faster.
    action_category("category") = this was in the spec, I'm assuming it's a category that action_names belong to.
    action_timestamp = when the action occurred, passed in through the request/api call.
        QUESTIONS TO PONDER: Do we want to/are we able to keep track of the timezone of the user? Or should we
        convert this to a Unix timestamp to potentially make querying faster?
    creation_date = time record was saved
    eye_data = various metadata around the event.  Use JSON so we can expand/contract the data without
        updating the DB structure.
    """

    id = models.BigAutoField(primary_key=True)
    session_id = models.CharField(max_length=255)
    entity_id = models.CharField(max_length=255)
    action_name = models.CharField(max_length=255)
    action_category = models.CharField(max_length=255)
    action_timestamp = models.DateTimeField()
    creation_date = models.DateTimeField(auto_now_add=True)
    eye_data = models.JSONField()

    def __str__(self):
        return f"{self.action_name} for entity {self.entity_id} on {self.action_timestamp}"

    # TODO: To perform better at scale, I would "save" using a task queue like celery
    def save(self, *args, **kwargs):
        super(Events, self).save(*args, **kwargs)
