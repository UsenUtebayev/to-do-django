# Generated by Django 4.1.7 on 2023-03-19 12:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['importance']},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['created_at']},
        ),
        migrations.AddField(
            model_name='category',
            name='importance',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
    ]
