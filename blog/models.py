from django.contrib.contenttypes.models import ContentType
from django.db import models
from core.models import BaseModel


class Post(BaseModel):
    title = models.CharField(max_length=255)
    excerpt = models.TextField(null=True)
    body = models.TextField(null=True)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.title
