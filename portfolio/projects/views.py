from django.shortcuts import render
from .models import Projects
from .serializer import ProjectsSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated



class ProjectsViewSet(viewsets.ModelViewSet):
    queryset=Projects.objects.all()
    serializer_class=ProjectsSerializer
    permission_classes=[]


# Create your views here.
