# Generated by Django 3.0.8 on 2020-11-03 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20201103_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sale_price',
            field=models.IntegerField(default=0),
        ),
    ]
