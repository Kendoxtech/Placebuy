# Generated by Django 5.0 on 2023-12-15 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_category_condition_message_offer_order_rating_seller_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Categorie',
        ),
        migrations.RenameModel(
            old_name='Transactions',
            new_name='Transaction',
        ),
    ]
