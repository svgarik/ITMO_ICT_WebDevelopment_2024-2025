# Generated by Django 5.1.2 on 2024-10-31 19:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0002_attribute_character_appearance_character_bennies_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charactersskill',
            name='bonus',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='charactersskill',
            name='value',
            field=models.SmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
