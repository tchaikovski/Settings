# Generated by Django 3.1.7 on 2021-08-02 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_auto_20210802_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slide',
            name='category',
        ),
        migrations.DeleteModel(
            name='Slider',
        ),
    ]
