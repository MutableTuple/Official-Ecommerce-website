# Generated by Django 4.0.6 on 2022-07-12 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_authentication_is_on_sale'),
    ]

    operations = [
        migrations.AddField(
            model_name='authentication',
            name='sale_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]