# Generated by Django 5.0.6 on 2024-07-08 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0039_spheres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата поступления'),
        ),
    ]
