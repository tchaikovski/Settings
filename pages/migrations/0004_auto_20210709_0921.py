# Generated by Django 3.1.7 on 2021-07-09 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_productsingle'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductSingle',
            new_name='Kontakt',
        ),
        migrations.AlterModelOptions(
            name='kontakt',
            options={'ordering': ('name',), 'verbose_name': 'Контакты', 'verbose_name_plural': 'Контакты'},
        ),
    ]
