"""
API V1: Posts Serializers
"""
###
# Libraries
###
from accounts.api.v1.serializers import BaseUserDetailsSerializer
from comments.api.v1.serializers import CommentSerializer
from posts.models import Post
from rest_framework import serializers


###
# Serializers
###
class PostSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    topic = serializers.ReadOnlyField(source='topic.urlname')
    user = BaseUserDetailsSerializer(read_only=True)

    def get_comments(self, instance):
        comments = instance.comments.all().order_by('-created_at')[:5]
        return CommentSerializer(comments, many=True).data
        
    class Meta:
        model = Post
        fields = '__all__'
