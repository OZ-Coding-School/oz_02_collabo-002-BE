# Generated by Django 5.0.6 on 2024-05-21 06:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_image_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 28, 6, 12, 32, 640009, tzinfo=datetime.timezone.utc)),
        ),
    ]
