# Generated by Django 3.0.6 on 2020-09-08 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_box_box_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='box',
            name='box_size',
        ),
        migrations.AddField(
            model_name='box',
            name='year_in_school',
            field=models.CharField(choices=[(10, 'Freshman'), (20, 'Sophomore'), (30, 'Junior'), (40, 'Senior')], default=10, max_length=2),
        ),
    ]
