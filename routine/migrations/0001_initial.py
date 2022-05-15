# Generated by Django 4.0.2 on 2022-05-15 14:09

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='routine',
            fields=[
                ('routine_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('goal', models.CharField(blank=True, max_length=100, null=True)),
                ('is_alarm', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='routine_result',
            fields=[
                ('routine_result_id', models.AutoField(primary_key=True, serialize=False)),
                ('result', models.CharField(blank=True, max_length=100, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('routine_day', models.CharField(blank=True, max_length=100, null=True)),
                ('routine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='routine.routine')),
            ],
        ),
        migrations.CreateModel(
            name='day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('routine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='routine.routine')),
            ],
        ),
    ]