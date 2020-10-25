# Generated by Django 3.0.6 on 2020-08-21 08:42

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_remove_box_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True, verbose_name='Видео'),
        ),
    ]
