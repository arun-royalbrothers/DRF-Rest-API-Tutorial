# Generated by Django 5.0.3 on 2024-05-20 06:45

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieReviewApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='review_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='released_year',
            field=models.DateField(),
        ),
    ]
