# Generated by Django 2.0.6 on 2018-08-30 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='stripe_id',
            field=models.CharField(blank=True, max_length=8),
        ),
    ]
