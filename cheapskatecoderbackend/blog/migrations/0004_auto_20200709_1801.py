# Generated by Django 3.0.7 on 2020-07-09 18:01

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_image',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to=blog.models._save_blog_upload_image_files),
        ),
    ]
