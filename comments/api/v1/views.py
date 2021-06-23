"""
API V1: Comments Views
"""
###
# Libraries
###
from posts.models import Post
from comments.api.v1.serializers import CommentSerializer
from comments.models import Comment
from rest_framework import permissions, viewsets
from rest_framework.exceptions import ValidationError

###
# Filters
###



###
# Viewsets
###
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def filter_queryset(self, queryset):
        return queryset.filter(post__pk=self.kwargs.get('post_pk'))

    def perform_create(self, serializer):
        try:
            post = Post.objects.get(pk=self.kwargs.get('post_pk'))
        except:
            raise ValidationError({'detail': "Post doesn't exist"})

        serializer.save(
            user=self.request.user,
            post=post
        )
