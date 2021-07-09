# Generated by Django 3.1.7 on 2021-07-09 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_category_updated'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSingle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('title', models.CharField(blank=True, max_length=170, null=True)),
                ('description', models.CharField(blank=True, max_length=300)),
                ('content', models.TextField(blank=True)),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Страница к главной',
                'verbose_name_plural': 'Страницы к главной',
                'ordering': ('name',),
                'index_together': {('id', 'slug')},
            },
        ),
    ]
