from django.db import models

# Create your models here.
from django.utils.text import slugify

from core.models import BaseModel


class Book(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    cover = models.CharField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Chapter(BaseModel):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to='chapter_backgrounds/', null=True, blank=True)
    chapter_number = models.PositiveIntegerField(default=1)
    game_icon = models.ImageField(upload_to='game_icons/', null=True, blank=True)
    content = models.TextField(null=True)

    class Meta:
        ordering = ['chapter_number']

    def __str__(self):
        return self.name
