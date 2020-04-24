from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.text import slugify
from markdownx.models import MarkdownxField

from core.models import BaseModel


class Post(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True)
    image = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    body = models.TextField(null=True)

    class Meta:
        ordering = ['-pk']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
