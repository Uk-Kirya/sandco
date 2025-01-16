# Generated by Django 5.0.6 on 2024-07-01 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_benefit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='benefit',
            name='title',
        ),
        migrations.AddField(
            model_name='benefit',
            name='icon',
            field=models.FileField(blank=True, upload_to='benefits/'),
        ),
    ]
