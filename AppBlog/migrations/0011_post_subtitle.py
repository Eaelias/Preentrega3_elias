# Generated by Django 4.2.7 on 2023-12-16 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0010_alter_post_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
