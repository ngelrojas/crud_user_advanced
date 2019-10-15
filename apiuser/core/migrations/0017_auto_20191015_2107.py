# Generated by Django 2.2.6 on 2019-10-15 21:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20191012_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biography',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 15, 21, 7, 43, 507801, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='biography',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 15, 21, 7, 43, 507846, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 15, 21, 7, 43, 501821, tzinfo=utc)),
        ),
    ]
