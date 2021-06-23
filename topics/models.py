"""
Topics Models
"""
###
# Libraries
###
from django.db import models
from django.utils.translation import gettext_lazy as _
from helpers.models import TimestampModel


###
# Choices
###


###
# Querysets
###


###
# Models
###
class Topic(TimestampModel):
    name = models.CharField(
        max_length=64, 
        verbose_name=_("name")
    )
    
    title = models.CharField(
        max_length=128, 
        verbose_name=_("title")
    )
    
    author = models.ForeignKey(
        'accounts.User', 
        on_delete=models.CASCADE,
        related_name="topics", 
        verbose_name=_("author")
    )
    
    description = models.CharField(
        max_length=500, 
        verbose_name=_("description")
    )
    
    urlname = models.SlugField(
        unique=True,
        verbose_name=_("urlname")
    )
