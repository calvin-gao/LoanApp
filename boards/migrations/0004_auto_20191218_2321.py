# Generated by Django 3.0 on 2019-12-19 07:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_auto_20191218_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='InceptionDate',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]