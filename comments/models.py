"""
Comments Models
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
class Comment(TimestampModel):
    title = models.CharField(
        max_length=128, 
        verbose_name=_('title')
    )
    
    content = models.CharField(
        max_length=500, 
        verbose_name=_('content')
    )

    post = models.ForeignKey(
        'posts.Post',
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name=_('post')
    )

    user = models.ForeignKey(
        'accounts.User', 
        on_delete=models.CASCADE,
        related_name="comments", 
        verbose_name=_("user")
    )