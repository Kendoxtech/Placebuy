# Generated by Django 5.0 on 2023-12-16 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0007_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='phone',
            field=models.IntegerField(max_length=20),
        ),
    ]
