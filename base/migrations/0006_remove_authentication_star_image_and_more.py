# Generated by Django 4.0.6 on 2022-07-06 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_authentication_item_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authentication',
            name='star_image',
        ),
        migrations.AddField(
            model_name='authentication',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
