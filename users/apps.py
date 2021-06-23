"""
Users Apps
"""
###
# Libraries
###
from django.apps import AppConfig


###
# Config
###
class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals
