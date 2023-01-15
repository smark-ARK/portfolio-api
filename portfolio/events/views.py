from django.shortcuts import render
from .models import Events
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated
from .serializer import EventsSerializer

# Create your views here.
class EventsViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Eventss.
    """
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    permission_classes = []