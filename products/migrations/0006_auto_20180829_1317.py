# Generated by Django 2.0.6 on 2018-08-29 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20180829_0851'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default='Enter Description')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='kunstenaar',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='artworks', to='products.Artist'),
            preserve_default=False,
        ),
    ]
