"""
API V1: Topics Serializers
"""
###
# Libraries
###
from accounts.api.v1.serializers import BaseUserDetailsSerializer
from topics.models import Topic
from rest_framework import serializers


###
# Serializers
###
class TopicSerializer(serializers.ModelSerializer):
    author = BaseUserDetailsSerializer(read_only=True)
    
    class Meta:
        model = Topic
        fields = "__all__"
