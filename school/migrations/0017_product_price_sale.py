# Generated by Django 3.1.7 on 2021-07-20 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0016_auto_20210720_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_sale',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
    ]
