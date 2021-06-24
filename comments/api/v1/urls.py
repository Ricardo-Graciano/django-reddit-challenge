"""
API V1: Comments Urls
"""
###
# Libraries
###
from .views import CommentViewSet

from django.urls import re_path, include
from posts.api.v1.urls import router as posts_router 
from rest_framework_nested import routers


###
# Routers
###
""" Main router """
router = routers.NestedSimpleRouter(posts_router, r'posts', lookup='post')
router.register(r'comments', CommentViewSet, 'topics-posts-comments')


###
# URLs
###
urlpatterns = [
    re_path(r'^', include(router.urls)),
]
