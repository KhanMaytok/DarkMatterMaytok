# Generated by Django 3.0.6 on 2020-06-16 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_chapter_rank_required'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='additional_js',
            field=models.TextField(null=True),
        ),
    ]
