# Generated by Django 2.2.7 on 2019-11-21 01:21

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('last_name', models.CharField(default='', max_length=255)),
                ('cellphone', models.CharField(default='', max_length=255)),
                ('dni', models.CharField(default='', max_length=100)),
                ('address', models.CharField(default='', max_length=300)),
                ('photo', models.CharField(blank=True, max_length=250)),
                ('type_user', models.IntegerField(choices=[(1, 'create user'), (2, 'contributor user')], default=1)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Campaing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug_title', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
                ('city', models.CharField(max_length=255)),
                ('budget', models.FloatField(blank=True, null=True)),
                ('qty_days', models.IntegerField(default=0)),
                ('facebook', models.CharField(blank=True, max_length=255)),
                ('twitter', models.CharField(blank=True, max_length=255)),
                ('linkedin', models.CharField(blank=True, max_length=255)),
                ('instagram', models.CharField(blank=True, max_length=255)),
                ('website', models.CharField(blank=True, max_length=255)),
                ('video', models.CharField(blank=True, max_length=255)),
                ('excerpt', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('public_at', models.DateTimeField(blank=True, null=True)),
                ('campaing_end_at', models.DateTimeField(blank=True, null=True)),
                ('add_date', models.DateTimeField(blank=True, null=True)),
                ('status_campaing', models.IntegerField(choices=[(0, 'begin'), (1, 'created'), (2, 'revision'), (3, 'public'), (4, 'completed')], default=0)),
                ('is_enabled', models.BooleanField(default=False)),
                ('is_complete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TagCampaing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('type_reward', models.IntegerField(choices=[(1, 'donation'), (2, 'contribution')], default=0)),
                ('delivery_data', models.DateTimeField()),
                ('delivery_place', models.CharField(blank=True, max_length=400)),
                ('description', models.CharField(blank=True, max_length=800)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('campaing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='campaing_reward', to='core.Campaing')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type_payment', models.IntegerField(choices=[(1, 'debit'), (2, 'credit'), (3, 'cash')], default=1)),
                ('status_payment', models.IntegerField(choices=[(1, 'init'), (2, 'pending'), (3, 'finish'), (4, 'devolution')], default=1)),
                ('code_payment', models.CharField(default='0', max_length=255)),
                ('budget_partial', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('campaing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Campaing')),
                ('reward', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Reward')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked', models.BooleanField(default=False)),
                ('campaing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Campaing')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CodeActivation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_token', models.CharField(blank=True, max_length=255)),
                ('is_expired', models.BooleanField(blank=True, default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryCampaing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('campaing', models.ManyToManyField(blank=True, related_name='category_campaing', to='core.Campaing')),
            ],
        ),
        migrations.AddField(
            model_name='campaing',
            name='tags',
            field=models.ManyToManyField(to='core.TagCampaing'),
        ),
        migrations.AddField(
            model_name='campaing',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_campaing', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Biography',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terms_cond', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('address_2', models.CharField(blank=True, max_length=255)),
                ('phone_number', models.CharField(blank=True, max_length=100)),
                ('email_2', models.CharField(blank=True, max_length=255)),
                ('b_facebook', models.CharField(blank=True, max_length=255)),
                ('b_twitter', models.CharField(blank=True, max_length=255)),
                ('b_linkedin', models.CharField(blank=True, max_length=255)),
                ('b_instagram', models.CharField(blank=True, max_length=255)),
                ('is_complete', models.BooleanField(default=False)),
                ('is_representative', models.BooleanField(default=False)),
                ('personal_website', models.CharField(blank=True, max_length=255)),
                ('company_website', models.CharField(blank=True, max_length=255)),
                ('company_name', models.CharField(blank=True, max_length=255)),
                ('company_nit', models.CharField(blank=True, max_length=255)),
                ('company_city', models.CharField(blank=True, max_length=255)),
                ('company_phone', models.CharField(blank=True, max_length=255)),
                ('company_address', models.CharField(blank=True, max_length=300)),
                ('company_email', models.CharField(blank=True, max_length=255)),
                ('company_logo', models.CharField(blank=True, max_length=255)),
                ('company_description', models.CharField(blank=True, max_length=255)),
                ('company_facebook', models.CharField(blank=True, max_length=255)),
                ('company_twitter', models.CharField(blank=True, max_length=255)),
                ('company_linkedin', models.CharField(blank=True, max_length=255)),
                ('company_instagram', models.CharField(blank=True, max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
