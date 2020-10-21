# Generated by Django 3.0.6 on 2020-09-10 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0019_postimage_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postimage',
            name='field',
        ),
        migrations.AddField(
            model_name='post1',
            name='field',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]