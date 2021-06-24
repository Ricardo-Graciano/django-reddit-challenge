"""
API V1: Topics Urls
"""
###
# Libraries
###
from .views import TopicViewSet

from django.urls import re_path, include
from rest_framework_nested import routers


###
# Routers
###
""" Main router """
router = routers.SimpleRouter()
router.register(r'topics', TopicViewSet, basename='topics')


###
# URLs
###
urlpatterns = [
    re_path(r'^', include(router.urls))
]
