# Generated by Django 4.0.6 on 2022-07-05 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_authentication_followers_authentication_star_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authentication',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='authentication',
            name='followers',
        ),
        migrations.RemoveField(
            model_name='authentication',
            name='last_name',
        ),
        migrations.AddField(
            model_name='authentication',
            name='item_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='authentication',
            name='item_name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
