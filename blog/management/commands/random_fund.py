from django.core.management.base import BaseCommand
from core.models import User
from random import randint
from blog.models import Project, ProjectUser
from django.db.models import Sum


class Command(BaseCommand):
    help = 'Init user'

    def handle(self, *args, **kwargs):
        count = User.objects.filter(is_founder=True).count()
        random_index = randint(0, count - 1)
        user = User.objects.filter(is_founder=True)[random_index]

        amount = randint(0, int(user.balance / 10000))

        project = Project.objects.get(pk=1)

        project_user, _ = ProjectUser.objects.get_or_create(project=project, user=user)
        project_user.amount += amount
        project_user.save()

        user.balance -= amount
        user.save()

        all_funds = ProjectUser.objects.filter(project=project).aggregate(Sum('amount'))['amount__sum']
        project.amount = all_funds
        project.save()
