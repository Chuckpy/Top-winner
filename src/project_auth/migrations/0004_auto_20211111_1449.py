# Generated by Django 3.1.8 on 2021-11-11 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_auth', '0003_remove_customer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date_of_birth',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
