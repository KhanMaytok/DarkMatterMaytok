from uuid import uuid4

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from core.models import BaseModel


class Post(BaseModel):
    title = models.CharField(max_length=255)
    uuid = models.UUIDField(default=uuid4, unique=True)

    def __str__(self):
        return self.title


class Comment(BaseModel, MPTTModel):
    body = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.body
