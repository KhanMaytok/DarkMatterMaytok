# Generated by Django 3.2.16 on 2022-11-24 04:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('blog', '0001_initial'), ('blog', '0002_auto_20200405_1848'), ('blog', '0003_delete_comment'), ('blog', '0004_comment'), ('blog', '0005_auto_20200410_1838'), ('blog', '0006_auto_20200421_1138'), ('blog', '0007_auto_20200421_2053'), ('blog', '0008_auto_20200423_2035'), ('blog', '0009_post_image'), ('blog', '0010_auto_20200423_2049'), ('blog', '0011_post_slug'), ('blog', '0012_auto_20200423_2152'), ('blog', '0013_auto_20200423_2209'), ('blog', '0014_auto_20200423_2221'), ('blog', '0016_remove_post_image'), ('blog', '0017_post_image'), ('blog', '0018_post_is_draft'), ('blog', '0019_alter_post_id'), ('blog', '0020_post_is_founder'), ('blog', '0021_rename_is_founder_post_is_founder_only'), ('blog', '0022_remove_post_is_founder_only'), ('blog', '0023_project_projectuser'), ('blog', '0024_post_project'), ('blog', '0025_alter_post_project'), ('blog', '0026_project_log')]

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Creado en')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Actualizado en')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(default='djangodbmodelsfieldscharfield', null=True)),
                ('amount', models.BigIntegerField(default=0, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('log', models.TextField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Creado en')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Actualizado en')),
                ('amount', models.BigIntegerField(default=0, null=True)),
                ('is_owner', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('project', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Creado en')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Actualizado en')),
                ('name', models.CharField(max_length=255)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('body', models.TextField(null=True)),
                ('description', models.TextField(null=True)),
                ('slug', models.SlugField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='post_headers/')),
                ('is_draft', models.BooleanField(default=True)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.project')),
            ],
            options={
                'abstract': False,
                'ordering': ['-pk'],
            },
        ),
    ]
