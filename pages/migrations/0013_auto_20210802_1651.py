# Generated by Django 3.1.7 on 2021-08-02 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_auto_20210802_1600'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Content',
        ),
        migrations.DeleteModel(
            name='Slide',
        ),
    ]
