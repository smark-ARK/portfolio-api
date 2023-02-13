from rest_framework import serializers
from .models import User


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
