# Generated by Django 5.0 on 2023-12-16 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0013_alter_amount_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment_method',
            name='name',
        ),
    ]