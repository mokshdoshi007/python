# Generated by Django 3.1.1 on 2020-12-30 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turfs', '0002_auto_20201230_2112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turfs',
            name='price',
        ),
        migrations.RemoveField(
            model_name='turfs',
            name='slots',
        ),
        migrations.AlterField(
            model_name='turfs',
            name='stars',
            field=models.FloatField(default=0),
        ),
    ]
