"""
API V1: Users Urls
"""
###
# Libraries
###
from django.urls import re_path, include
from rest_framework_nested import routers


###
# Routers
###
""" Main router """
router = routers.SimpleRouter()


###
# URLs
###
urlpatterns = [
    re_path(r'^', include(router.urls)),
]
