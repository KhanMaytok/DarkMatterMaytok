from django.contrib.contenttypes.models import ContentType
from django.db import models
from core.models import BaseModel


class Post(BaseModel):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255, null=True)
    excerpt = models.TextField(null=True)
    body = models.TextField(null=True)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.name
