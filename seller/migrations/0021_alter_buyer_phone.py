# Generated by Django 5.0 on 2023-12-17 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0020_buyer_email_buyer_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='phone',
            field=models.IntegerField(max_length=20, null=True),
        ),
    ]
