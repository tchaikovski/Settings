# Generated by Django 3.1.7 on 2021-07-12 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0010_auto_20210712_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='shablon',
            field=models.CharField(choices=[('school/product/list.html', 'Base'), ('school/product/school_list.html', 'School'), ('school/product/list1.html', 'Staff'), ('school/product/list2.html', 'Quotes'), ('school/product/list3.html', 'Not name')], max_length=500),
        ),
    ]
