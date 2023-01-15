from rest_framework import serializers 
from .models import Skills,Tools

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Skills
        fields="__all__"

class ToolsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Skills
        fields="__all__"