# Generated by Django 2.2.6 on 2019-10-12 21:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20191012_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biography',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 12, 21, 55, 42, 821709, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='biography',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 12, 21, 55, 42, 821742, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 12, 21, 55, 42, 817922, tzinfo=utc)),
        ),
    ]