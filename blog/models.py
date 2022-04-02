from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from core.models import BaseModel


class Post(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True)
    image = models.ImageField(upload_to='post_headers/', null=True, blank=True)
    description = models.TextField(null=True)
    body = models.TextField(null=True)
    is_draft = models.BooleanField(default=True)
    is_founder = models.BooleanField(default=False)

    class Meta:
        ordering = ['-pk']

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    @property
    def admin_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(self.id,))

    def get_absolute_url(self):
        return reverse('blog_post', kwargs={'pk': self.pk, 'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
