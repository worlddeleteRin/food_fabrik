# Generated by Django 3.1.3 on 2021-03-26 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0046_auto_20210326_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_bonus_use',
            field=models.BooleanField(default=True),
        ),
    ]
