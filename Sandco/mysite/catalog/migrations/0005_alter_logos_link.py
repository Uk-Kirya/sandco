# Generated by Django 5.0.6 on 2024-06-20 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_logos_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logos',
            name='link',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]