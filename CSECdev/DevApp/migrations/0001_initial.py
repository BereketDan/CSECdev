# Generated by Django 4.2.5 on 2023-11-27 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventName', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('hour', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Telegram_username', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=255)),
                ('messageDate', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fisrtname', models.CharField(max_length=255)),
                ('ugr', models.CharField(max_length=255)),
                ('sex', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('year', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User_auth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]