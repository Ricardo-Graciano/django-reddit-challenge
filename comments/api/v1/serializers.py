"""
API V1: Comments Serializers
"""
###
# Libraries
###
from accounts.api.v1.serializers import BaseUserDetailsSerializer
from comments.models import Comment
from rest_framework import serializers


###
# Serializers
###
class CommentSerializer(serializers.ModelSerializer):
    post = serializers.ReadOnlyField(source='post.pk')
    user = BaseUserDetailsSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = '__all__'
