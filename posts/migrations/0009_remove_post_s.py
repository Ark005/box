# Generated by Django 3.0.6 on 2020-09-08 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_post_s'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='s',
        ),
    ]