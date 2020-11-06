# Generated by Django 3.0.8 on 2020-11-06 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0009_order_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery',
            field=models.CharField(default='', max_length=200),
        ),
    ]
