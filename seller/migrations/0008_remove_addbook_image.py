# Generated by Django 3.2.6 on 2021-08-29 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0007_addbook_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addbook',
            name='image',
        ),
    ]
