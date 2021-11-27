from django.http.response import JsonResponse

from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from .serializers import EventsSerializer
from consumeraffairs.models import Events


class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all().order_by('action_timestamp')
    serializer_class = EventsSerializer


@api_view(['POST'])
def events_create(request):
    events_data = JSONParser().parse(request)
    events_serializer = EventsSerializer(data=events_data)
    if events_serializer.is_valid():
        # TODO: I would use a task queue w/ caching to save events to improve performance at "scale".
        events_serializer.save()
        return JsonResponse(events_serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def events_detail(request, pk):
    try:
        event = Events.objects.get(pk=pk)
    except Events.DoesNotExist:
        return JsonResponse({'message': 'The event does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        event_serializer = EventsSerializer(event)
        return JsonResponse(event_serializer.data)


# TODO: GET by session_id (user), entity_id (site, app, etc.) or
#  action_name/category, sorted by date_range (default to last 30 days)
@api_view(['GET'])
def events_series(request):
    content = {'message': 'Series not implemented'}
    return JsonResponse(content, status=status.HTTP_501_NOT_IMPLEMENTED)
