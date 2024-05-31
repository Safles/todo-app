from rest_framework import serializers
from .models import todoLIST

class todoListSerializer(serializers.ModelSerializer):
    class Meta:
        model=todoLIST
        fields='__all__'