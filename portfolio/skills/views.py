from django.shortcuts import render
from rest_framework import viewsets
from .models import Skills,Tools
from .serializer import SkillsSerializer,ToolsSerializer
from rest_framework.permissions import IsAuthenticated

class SkillsViewSet(viewsets.ModelViewSet):
    queryset=Skills.objects.all()
    serializer_class=SkillsSerializer
    permission_classes=[]


class ToolsViewSet(viewsets.ModelViewSet):
    queryset=Tools.objects.all()
    serializer_class=ToolsSerializer
    permission_classes=[]
# Create your views here.
