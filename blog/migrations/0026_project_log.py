# Generated by Django 3.2.13 on 2022-05-07 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_alter_post_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='log',
            field=models.TextField(null=True),
        ),
    ]