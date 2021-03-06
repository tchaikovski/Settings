# Generated by Django 3.1.7 on 2021-08-01 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='cars/%Y/%m/%d')),
                ('title', models.CharField(blank=True, max_length=170, null=True)),
                ('description', models.CharField(blank=True, max_length=300)),
                ('available', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ('name',),
                'index_together': {('id', 'slug')},
            },
        ),
    ]
