# Generated by Django 3.2.4 on 2021-06-18 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0022_auto_20210611_0016'),
    ]

    operations = [
        migrations.AddField(
            model_name='gladiator',
            name='health',
            field=models.DecimalField(decimal_places=3, default=1.1, max_digits=10),
        ),
        migrations.AddField(
            model_name='gladiator',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='gladiators/'),
        ),
        migrations.AddField(
            model_name='gladiator',
            name='meditation',
            field=models.DecimalField(decimal_places=3, default=1.1, max_digits=10),
        ),
    ]