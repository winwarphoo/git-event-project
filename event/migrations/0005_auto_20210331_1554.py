# Generated by Django 3.1.7 on 2021-03-31 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_auto_20210329_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventattendence',
            name='email',
            field=models.EmailField(blank=True, max_length=70, unique=True),
        ),
    ]