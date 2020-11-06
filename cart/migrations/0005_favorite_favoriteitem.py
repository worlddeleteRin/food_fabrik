# Generated by Django 3.0.8 on 2020-10-29 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_item_sale_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('session_key', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Favoriteitem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pr_id', models.IntegerField(default=None)),
                ('favorite', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.Favorite')),
            ],
        ),
    ]
