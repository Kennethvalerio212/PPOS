# Generated by Django 3.2.9 on 2021-11-11 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sales', '0002_alter_product_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
