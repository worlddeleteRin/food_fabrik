# Generated by Django 3.1.3 on 2021-02-23 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0011_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='bonus_gained',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]