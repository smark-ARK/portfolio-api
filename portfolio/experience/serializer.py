# from dataclasses import field
from rest_framework import serializers
from .models import Experience,Company


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = "__all__"

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fiels="__all__"