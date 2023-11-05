# Generated by Django 4.2.7 on 2023-11-04 16:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_rename_categories_category_rename_comments_comment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.CharField(default='Unknown', max_length=30),
        ),
        migrations.AddField(
            model_name='comment',
            name='body',
            field=models.TextField(default='commentless'),
        ),
        migrations.AddField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 1, 1, 12, 12, 12, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.TextField(default='bodyless'),
        ),
        migrations.AddField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 1, 1, 12, 12, 13, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='Untitled', max_length=30),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_text',
            field=models.CharField(default='Unnamed', max_length=30),
        ),
    ]