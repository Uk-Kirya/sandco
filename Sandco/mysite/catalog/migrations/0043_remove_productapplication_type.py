# Generated by Django 5.0.6 on 2024-08-05 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0042_application_type_productapplication_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productapplication',
            name='type',
        ),
    ]
