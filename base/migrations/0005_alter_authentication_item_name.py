# Generated by Django 4.0.6 on 2022-07-05 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_authentication_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authentication',
            name='item_name',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
