# Generated by Django 2.1.5 on 2019-02-12 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_img',
            field=models.CharField(default='', max_length=255),
        ),
    ]