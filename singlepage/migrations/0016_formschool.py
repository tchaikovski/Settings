# Generated by Django 3.1.7 on 2021-08-03 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('singlepage', '0015_auto_20210803_0953'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormSchool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
    ]
