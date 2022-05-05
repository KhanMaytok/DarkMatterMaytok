import uuid

from django.core.management.base import BaseCommand
from core.models import User


class Command(BaseCommand):
    help = 'Create fake users to poblate posts'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        user = User.objects.create_user(username=username, password=uuid.uuid4(),
                                        email=f'{username}@{username}.{username}')
        user.is_founder = True
        user.save()
