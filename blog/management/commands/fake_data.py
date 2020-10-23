from django.core.management.base import BaseCommand
from django.utils.text import slugify

from blog.models import Post
from faker import Faker


class Command(BaseCommand):
    help = 'Init user'

    def handle(self, *args, **kwargs):
        fake = Faker()
        arr = []
        for i in range(5000):
            body = f"<p>{fake.paragraph(nb_sentences=10)}</p>" \
                   f'<img src="https://s3.maytok.com/maytokmedia/django-summernote/2020-10-02/55d4359c-afb3-49a9-9b06-a85d734db8f8.jpg" class="img-fluid">' \
                   f'<span class="caption text-muted">La lista se irá expandiendo</span>' \
                   f"<p>{fake.paragraph(nb_sentences=10)}</p>" \
                   f"<p>{fake.paragraph(nb_sentences=10)}</p>"
            name = fake.paragraph(nb_sentences=1),
            post = Post(
                name=name,
                description=fake.paragraph(nb_sentences=3),
                body=body,
                slug=slugify(name)
            )
            arr.append(post)

        Post.objects.bulk_create(arr)
