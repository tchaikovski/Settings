# Generated by Django 3.1.7 on 2021-08-02 15:30

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20210801_1827'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='pages',
            name='category',
            field=mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.category'),
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('description', models.CharField(blank=True, max_length=300)),
                ('content', models.TextField(blank=True)),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.slider')),
            ],
        ),
    ]