"""
API V1: Topics Urls
"""
###
# Libraries
###
from django.urls import re_path, include
from rest_framework_nested import routers

from comments.api.v1.views import CommentViewSet
from posts.api.v1.views import PostViewSet
from topics.api.v1.views import TopicViewSet


###
# Routers
###
""" Main router """
router = routers.SimpleRouter()
router.register(r'topics', TopicViewSet, basename='topics')

posts_router = routers.NestedSimpleRouter(router, r'topics', lookup='topic')
posts_router.register(r'posts', PostViewSet, basename='topics-posts')

comments_router = routers.NestedSimpleRouter(posts_router, r'posts', lookup='post')
comments_router.register(r'comments', CommentViewSet, 'topics-posts-comments')


###
# URLs
###
urlpatterns = [
    re_path(r'^', include(router.urls)),
    re_path(r'^', include(posts_router.urls)),
    re_path(r'^', include(comments_router.urls)),
]
