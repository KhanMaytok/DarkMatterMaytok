# Generated by Django 3.0.6 on 2020-06-16 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_chapter_additional_js'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter',
            name='additional_js',
        ),
    ]
