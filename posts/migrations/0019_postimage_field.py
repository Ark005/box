# Generated by Django 3.0.6 on 2020-09-10 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0018_auto_20200910_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='postimage',
            name='field',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
