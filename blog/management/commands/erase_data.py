from django.core.management.base import BaseCommand

from blog.models import Post
from faker import Faker


class Command(BaseCommand):
    help = 'Init user'

    def handle(self, *args, **kwargs):
        Post.objects.all().delete()
