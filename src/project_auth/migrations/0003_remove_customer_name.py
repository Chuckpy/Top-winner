# Generated by Django 3.1.8 on 2021-11-09 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_auth', '0002_auto_20211109_1928'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='name',
        ),
    ]
