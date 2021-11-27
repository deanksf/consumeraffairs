from rest_framework import serializers

from consumeraffairs.models import Events


class EventsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Events
        fields = ('session_id', 'entity_id', 'action_name', 'action_category', 'action_timestamp', 'eye_data')