from django.core.management.base import BaseCommand
from django.utils.text import slugify

from blog.models import Post
from faker import Faker


class Command(BaseCommand):
    help = 'Create fake users to poblate posts'

    def handle(self, *args, **kwargs):
        fake = Faker()
        arr = []
        for i in range(200):
            pass

        Post.objects.bulk_create(arr)
