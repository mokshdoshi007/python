# Generated by Django 3.1.1 on 2020-12-30 18:00

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turfs', '0003_auto_20201230_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='turfs',
            name='price',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='turfs',
            name='slots',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), size=None), blank=True, null=True, size=None),
        ),
    ]
