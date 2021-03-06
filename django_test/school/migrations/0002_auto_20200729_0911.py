# Generated by Django 2.2.14 on 2020-07-29 09:11

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='school',
            name='established_in',
            field=models.IntegerField(default=2020, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2020)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='school',
            name='last_modified_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='location',
            field=models.CharField(default='Neverland', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='last_modified_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='nationality',
            field=models.CharField(default='kazakh', max_length=20),
            preserve_default=False,
        ),
    ]
