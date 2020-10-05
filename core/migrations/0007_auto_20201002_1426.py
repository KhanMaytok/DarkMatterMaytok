# Generated by Django 3.1.1 on 2020-10-02 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20201002_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rank',
            field=models.CharField(choices=[('0', 'IRON'), ('1', 'BRONZE'), ('2', 'SILVER'), ('3', 'GOLD'), ('4', 'PLATINUM'), ('5', 'DIAMOND'), ('6', 'MASTER'), ('7', 'GRANDMASTER'), ('8', 'CHALLENGER')], default='0', max_length=50),
        ),
    ]