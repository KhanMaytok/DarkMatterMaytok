# Generated by Django 3.0.6 on 2020-06-16 19:01

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0014_remove_chapter_additional_js'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='sounds',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
    ]
