# Generated by Django 5.0.6 on 2024-08-05 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0043_remove_productapplication_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='type',
        ),
        migrations.AddField(
            model_name='application',
            name='category',
            field=models.CharField(blank=True, max_length=100, verbose_name='Направление'),
        ),
    ]