"""
API V1: Posts Views
"""
###
# Libraries
###
from helpers.permissions import IsOwnerOrReadOnly
from posts.api.v1.serializers import PostSerializer
from posts.models import Post
from rest_framework import permissions, viewsets
from rest_framework.exceptions import ValidationError
from topics.models import Topic


###
# Filters
###


###
# Viewsets
###
class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def filter_queryset(self, queryset):
        return queryset.filter(topic__urlname=self.kwargs.get('topic_urlname'))

    def perform_create(self, serializer):
        try:
            topic = Topic.objects.get(urlname=self.kwargs.get('topic_urlname'))
        except:
            raise ValidationError({'detail': "Topic doesn't exist"})

        serializer.save(
            user=self.request.user,
            topic=topic
        )