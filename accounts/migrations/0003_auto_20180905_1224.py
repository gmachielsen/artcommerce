# Generated by Django 2.0.6 on 2018-09-05 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_seller_stripe_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyer',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='buyer',
            name='email',
            field=models.EmailField(blank=True, max_length=70),
        ),
        migrations.AddField(
            model_name='seller',
            name='email',
            field=models.EmailField(blank=True, max_length=70),
        ),
    ]
