# Generated by Django 2.2.6 on 2019-11-06 20:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20191106_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
