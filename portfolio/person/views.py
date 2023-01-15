from django.shortcuts import render
from .models import Person
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated
from .serializer import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset=Person.objects.all()
    serializer_class=PersonSerializer
    permission_classes=[]
# Create your views here.
