# Generated by Django 4.0 on 2022-01-31 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(blank='True', default='', max_length=300),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(blank='True', default='', max_length=20),
        ),
    ]