# Generated by Django 5.0 on 2023-12-15 15:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('product_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('condition', models.CharField(choices=[('N', 'New'), ('O', 'Old'), ('D', 'Damaged')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=1000)),
                ('time', models.TimeField()),
                ('datetime', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('discount', models.FloatField()),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer', models.CharField(max_length=255)),
                ('product', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('order_date', models.DateField()),
                ('order_status', models.CharField(max_length=20)),
                ('payment_method', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=255)),
                ('buyer', models.CharField(max_length=255)),
                ('comment', models.CharField(max_length=255)),
                ('time', models.TimeField()),
                ('datetime', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('image_url', models.CharField(max_length=2083)),
                ('address', models.CharField(max_length=255)),
                ('bio', models.CharField(max_length=255)),
                ('website', models.URLField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer', models.CharField(max_length=255)),
                ('product', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('payment_method', models.CharField(max_length=255)),
                ('datetime', models.DateField()),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='seller.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='condition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='seller.condition'),
        ),
    ]
