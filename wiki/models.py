from django.db import models
from django.utils.text import slugify
from martor.models import MartorField

from core.models import BaseModel


class Infobox(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Article(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    content = MartorField()
    infobox = models.ForeignKey(Infobox, on_delete=models.SET_NULL, null=True, blank=True)
    infobox_content = models.JSONField(default=dict, blank=True)
    is_draft = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
            super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
