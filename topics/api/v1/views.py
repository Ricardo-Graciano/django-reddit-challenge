"""
API V1: Topics Views
"""
###
# Libraries
###
from .serializers import TopicSerializer

from rest_framework import permissions, viewsets
from topics.api.v1.permissions import IsOwnerOrReadOnly
from topics.models import Topic


###
# Filters
###


###
# Viewsets
###
class TopicViewSet(viewsets.ModelViewSet):
    lookup_field = 'urlname'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)