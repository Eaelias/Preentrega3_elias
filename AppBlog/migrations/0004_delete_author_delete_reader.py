# Generated by Django 4.2.7 on 2023-12-12 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0003_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Reader',
        ),
    ]