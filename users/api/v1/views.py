"""
API V1: Users Views
"""
###
# Libraries
###
from .serializers import UserSerializer

from django.contrib.auth.models import User
from rest_framework import viewsets

###
# Filters
###


###
# Viewsets
###
class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
