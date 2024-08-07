# Generated by Django 5.0.6 on 2024-07-04 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0038_application'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spheres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='Заголовок')),
                ('image', models.FileField(blank=True, upload_to='spheres/', verbose_name='Картинка')),
                ('link', models.CharField(blank=True, max_length=100, verbose_name='Ссылка на библиотеку')),
                ('order', models.IntegerField(blank=True, default=0, max_length=100, verbose_name='Порядковый номер')),
            ],
            options={
                'verbose_name': 'Сфера',
                'verbose_name_plural': 'Сферы применения',
            },
        ),
    ]
