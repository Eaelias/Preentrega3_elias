# Generated by Django 4.2.7 on 2023-12-11 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='uncategorized', max_length=255),
        ),
    ]
