# Generated by Django 3.0.6 on 2020-09-08 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20200908_0715'),
    ]

    operations = [
        migrations.AddField(
            model_name='box',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
