# Generated by Django 5.0 on 2023-12-17 00:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0018_remove_status_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='status',
            old_name='status',
            new_name='status_name',
        ),
    ]
