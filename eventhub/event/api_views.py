from rest_framework import  generics

from event.models import Event
from event.serializers import EventSerializer


class EventAPIView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
