from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.text import slugify

from DarkMatterMaytok.settings import USER_RANK
from core.models import BaseModel


class Book(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    cover = models.CharField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Book, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('book_show', kwargs={'pk': self.pk, 'slug': self.slug})

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
    rank_required = models.CharField(max_length=50, choices=USER_RANK, default='X')

    class Meta:
        ordering = ['chapter_number']

    def get_absolute_url(self):
        return reverse('chapter_show',
                       kwargs={'pk': self.book.pk, 'slug': self.book.slug, 'chapter_number': self.chapter_number})

    def __str__(self):
        return self.name
