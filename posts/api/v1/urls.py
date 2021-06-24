"""
API V1: Posts Urls
"""
###
# Libraries
###
from .views import PostViewSet

from django.urls import re_path, include
from rest_framework_nested import routers
from topics.api.v1.urls import router as topics_router


###
# Routers
###
""" Main router """
router = routers.NestedSimpleRouter(topics_router, r'topics', lookup='topic')
router.register(r'posts', PostViewSet, basename='topics-posts')


###
# URLs
###
urlpatterns = [
    re_path(r'^', include(router.urls)),
]
