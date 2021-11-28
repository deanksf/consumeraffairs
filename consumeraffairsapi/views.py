from rest_framework import serializers, viewsets
from .serializers import EventsSerializer
from consumeraffairs.models import Events


class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all().order_by('action_timestamp')
    serializer_class = EventsSerializer