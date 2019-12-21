# Generated by Django 3.0 on 2019-12-19 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_snippet_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='Business_Address',
        ),
        migrations.RemoveField(
            model_name='owners',
            name='HomeAddress',
        ),
        migrations.AddField(
            model_name='business',
            name='Address1',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='business',
            name='Address2',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='business',
            name='City',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='business',
            name='State',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='business',
            name='Zip',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]