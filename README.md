# ConsumerAffairs Practical Test Solution
## Building 'The Eye'
Given the requirements for The Eye, I used the Django Rest Framework (DRF) as it provides and API that can be used by multiple websites as well as potential future use-cases such as apps and third-party integrations.  For full transparency, while I've worked with the DRF this was my first time installing it.  It took some time but I felt it was the best solution.

## Problem Requirements -> Soution Details
- *An Event has a category, a name and a payload of data (the payload can change according to which event an Application is sending)*
  - The model has an 'action_category', 'action_name' and 'eye_data' column. 
- *Different types of Events (identified by category + name) can have different validations for their payloads*
  - The serializer has placeholder functions to build custom validation
- *An Event is associated to a Session*
  - The model has a column for 'session_id'
- *Events in a Session should be sequential and ordered by the time they occurred*
  - The model has an 'action_timestamp' which is required from the external source as well as an auto generated 'creation_date'
- *The Application sending events is responsible for generating the Session identifier*
  - The 'session_id' is required by the API POST
- *Applications should be recognized as "trusted clients" to "The Eye"*
  - BIG NOTE:  I did not implement anything beyond basic authentication provided through the web interface (ran out of time).  
    - I would implement standard OAuth
    - An authenticated user can POST events
    - An authenticated user can only GET events they've submitted
    - I need to expand the model and add 'user_id'
- *Applications can send events for the same session*
  - 'session_id' does not need to be unique
- *"The Eye" will be receiving, in average, ~100 events/second, so consider not processing events in real time*
  - There's a comment in models.py regarding using a cache based task queue to save the records.  I'm not sure that the model is the best place for this, but I wanted to create a starting point for this mechanism.  
- *When Applications talk to "The Eye", make sure to not leave them hanging*
  - For now we're using the default API responses and, while using the caching/task mechanism, the API would respond once the job is in the queue.  The issue here is that the user could receive a confirmation that the record was saved when in fact it wasn't (should something happen to the task queue).  I would work with the product team to determine what our Service Level Agreement for this product is and scale the app to meet those requirements.
- *Your application is dockerized*
  - My app is dockerized 

## ADDITIONAL COMMENTS
There are a number of comments in the code to further explain my thinking, ask further questions and offer options for various solutions for those questions.

## TODO:
- Testing
- Typing/Type Hints

