from rest_framework import generics
from .models import Event, Sermon
from .serializers import EventSerializer, SermonSerializer

class EventListCreate(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class SermonListCreate(generics.ListCreateAPIView):
    queryset = Sermon.objects.all()
    serializer_class = SermonSerializer