# Generated by Django 3.0.6 on 2020-09-10 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0017_auto_20200910_1140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='field',
            old_name='field_name',
            new_name='field',
        ),
    ]