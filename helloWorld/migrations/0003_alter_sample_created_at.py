# Generated by Django 5.0.3 on 2024-04-03 07:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloWorld', '0002_sample_is_active_alter_sample_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 3, 13, 21, 49, 804936)),
        ),
    ]
