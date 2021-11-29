import json

from rest_framework import serializers

from consumeraffairs.models import Events


# TODO:  At scale, the read serializer can slow down performance.  I need to create a simple
#  read-only serializer similar to the example here: https://hakibenita.com/django-rest-framework-slow
class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ('session_id', 'entity_id', 'action_name', 'action_category', 'action_timestamp', 'eye_data')

    # If we want to allow only certain actions/activites to belong to certain categories, we can enforce
    # that validation here.  I would store these in the DB and create a UI so someone can maintain these.
    ACTION_CATEGORIES = {
        'web': ['register', 'login', 'view_page'],
        'app': ['open', 'search']
    }

    def validate_action_name(self, value):
        category = self.initial_data.__getitem__('action_category')
        if value not in self.ACTION_CATEGORIES[category]:
            raise serializers.ValidationError(f"'action_name': '{value}' does not belong to 'action_category': '{category}'.")
        return value

    # TODO: This is where custom validation can occur depending upon the action_name or action_category
    def custom_validation(self):
        pass