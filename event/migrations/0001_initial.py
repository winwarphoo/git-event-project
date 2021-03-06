# Generated by Django 3.1.7 on 2021-03-26 10:11

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
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('about', models.TextField(help_text='Enter about of event')),
                ('date_of_start', models.DateField(blank=True, null=True)),
                ('date_of_end', models.DateField(blank=True, null=True, verbose_name='ended')),
            ],
            options={
                'ordering': ['date_of_start'],
            },
        ),
        migrations.CreateModel(
            name='EventCreator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user', 'date_of_birth'],
            },
        ),
        migrations.CreateModel(
            name='EventAttendence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ImageField(default='defo', upload_to='images/')),
                ('name', models.TextField(help_text='Enter your Name', max_length=1000)),
                ('email', models.EmailField(blank=True, max_length=70, unique=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('phone_no', models.CharField(max_length=12)),
                ('event', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='event.event')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='event',
            name='teacher',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='event.eventcreator'),
        ),
    ]
