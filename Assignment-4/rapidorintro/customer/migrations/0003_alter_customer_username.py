# Generated by Django 3.2.5 on 2021-07-12 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customer_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='username',
            field=models.CharField(default='sanu', max_length=20, unique=True),
            preserve_default=False,
        ),
    ]
