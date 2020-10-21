# Generated by Django 3.0.6 on 2020-09-21 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0033_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foo', models.PositiveIntegerField(choices=[('1', 'Cheers'), ('2', 'The Blue Oyster')])),
            ],
        ),
        migrations.AlterField(
            model_name='box',
            name='box_size',
            field=models.CharField(choices=[('240х185х120', '240х185х120'), ('270х220х70', '270х220х70')], default='50х50х35', max_length=20),
        ),
        migrations.AlterField(
            model_name='box1',
            name='box_size1',
            field=models.CharField(choices=[('240х185х120', '240х185х120'), ('270х220х70', '270х220х70')], default='50х50х35', max_length=20),
        ),
    ]