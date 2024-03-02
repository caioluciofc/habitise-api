# Generated by Django 5.0.2 on 2024-03-02 16:17

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habitise', '0006_habitmodel_emoji_unicode_hex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='negative_habits',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(null=True), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='user',
            name='positive_habits',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(null=True), default=list, size=None),
        ),
    ]