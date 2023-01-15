from django.shortcuts import render
from .models import Experience,Company
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated
from .serializer import ExperienceSerializer,CompanySerializer

# Create your views here.
class ExperienceViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Eventss.
    """
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = []


class CompanyViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Eventss.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = []
# Create your views here.
