# Generated by Django 3.2.5 on 2021-07-09 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20210709_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tax_percent',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit_price',
            field=models.FloatField(),
        ),
    ]
