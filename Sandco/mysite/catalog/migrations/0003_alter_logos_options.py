# Generated by Django 5.0.6 on 2024-06-20 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_logos_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='logos',
            options={'verbose_name': 'Логотип', 'verbose_name_plural': 'Логотипы'},
        ),
    ]
