# Generated by Django 5.0 on 2023-12-16 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0014_remove_payment_method_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amount',
            name='amount',
            field=models.FloatField(),
        ),
    ]