# Generated by Django 5.0 on 2023-12-15 21:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0005_transaction_status_alter_transaction_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='seller.amount'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.amount'),
        ),
    ]
