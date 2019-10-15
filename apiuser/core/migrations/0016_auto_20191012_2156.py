# Generated by Django 2.2.6 on 2019-10-12 21:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20191012_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biography',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 12, 21, 56, 51, 57602, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='biography',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 12, 21, 56, 51, 57698, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 12, 21, 56, 51, 53485, tzinfo=utc)),
        ),
    ]
