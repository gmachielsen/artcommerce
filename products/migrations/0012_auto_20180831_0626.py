# Generated by Django 2.0.6 on 2018-08-31 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20180831_0614'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='width',
            new_name='Width_of_object_in_CM',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='length',
            new_name='length_of_object_in_CM',
        ),
    ]
