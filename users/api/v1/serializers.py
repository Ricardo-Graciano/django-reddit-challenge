"""
API V1: Users Serializers
"""
###
# Libraries
###
from django.contrib.auth.models import User
from rest_framework import serializers


###
# Serializers
###
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = "__all__"
