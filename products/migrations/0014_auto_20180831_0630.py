# Generated by Django 2.0.6 on 2018-08-31 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20180831_0630'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='WidthCM',
            new_name='widthCM',
        ),
    ]