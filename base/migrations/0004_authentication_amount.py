# Generated by Django 4.0.6 on 2022-07-05 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_authentication_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='authentication',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
