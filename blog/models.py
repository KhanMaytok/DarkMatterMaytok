from uuid import uuid4

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from core.models import BaseModel


class Post(BaseModel):
    title = models.CharField(max_length=255)
    excerpt = models.TextField(null=True)
    body = models.TextField(null=True)

    def __str__(self):
        return self.title
