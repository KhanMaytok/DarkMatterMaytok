# Generated by Django 3.1.1 on 2020-10-02 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200505_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rank',
            field=models.CharField(choices=[('0', 'IRON'), ('1', 'BRONZE'), ('2', 'SILVER'), ('3', 'GOLD'), ('4', 'PLATINUM'), ('5', 'DIAMOND'), ('6', 'MASTER'), ('7', 'GRANDMASTER'), ('8', 'CHALLENGER')], default='X', max_length=50),
        ),
    ]
