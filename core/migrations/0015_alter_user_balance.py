# Generated by Django 3.2.13 on 2022-05-05 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_user_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='balance',
            field=models.BigIntegerField(default=65000000000),
        ),
    ]
