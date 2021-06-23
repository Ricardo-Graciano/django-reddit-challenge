"""
Posts Models
"""
###
# Libraries
###
from helpers.models import TimestampModel
from django.db import models
from django.utils.translation import gettext_lazy as _

###
# Choices
###


###
# Querysets
###


###
# Models
###
class Post(TimestampModel):
    title = models.CharField(
        max_length=128, 
        verbose_name=_('title')
    )
    
    content = models.CharField(
        max_length=500, 
        verbose_name=_('content')
    )

    topic = models.ForeignKey(
        'topics.Topic',
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name=_('topic')
    )

    user = models.ForeignKey(
        'accounts.User', 
        on_delete=models.CASCADE,
        related_name="posts", 
        verbose_name=_("user")
    )

