# Generated by Django 3.1.7 on 2021-07-27 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20210726_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='gos',
            field=models.CharField(blank=True, max_length=200, verbose_name='Гос Номер'),
        ),
    ]
