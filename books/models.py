from django.db import models

# Create your models here.
from django.utils.text import slugify

from core.models import BaseModel


class Book(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True)
    cover = models.CharField(max_length=255, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Chapter(BaseModel):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    number = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name
