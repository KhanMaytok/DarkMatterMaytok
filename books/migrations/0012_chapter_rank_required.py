# Generated by Django 3.0.5 on 2020-05-05 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_chapter_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='rank_required',
            field=models.CharField(choices=[('X', 'COURTIER'), ('B', 'BARON'), ('C', 'COUNT'), ('D', 'DUKE'), ('K', 'KING'), ('E', 'EMPEROR')], default='X', max_length=50),
        ),
    ]