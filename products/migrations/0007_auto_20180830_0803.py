# Generated by Django 2.0.6 on 2018-08-30 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20180829_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='thema',
            field=models.CharField(choices=[('X', 'Kies jouw thema'), ('A', 'Architectuur'), ('D', 'Dieren'), ('E', 'Eten en Drinken'), ('L', 'Land en Cultuur'), ('M', 'Mens en Portret'), ('O', 'Overig')], default='X', max_length=1),
        ),
        migrations.AlterField(
            model_name='product',
            name='prijstype',
            field=models.CharField(choices=[('X', 'Kies prijstype'), ('B', 'Geen voorkeur'), ('K', 'Koop'), ('H', 'Huur')], default='X', max_length=1),
        ),
        migrations.AlterField(
            model_name='product',
            name='stijl',
            field=models.CharField(choices=[('X', 'Kies jouw kunststijl'), ('R', 'Realistisch'), ('I', 'Imprestionistisch'), ('A', 'Abstract'), ('E', 'Expressionistisch'), ('F', 'Figuratief')], default='X', max_length=1),
        ),
    ]