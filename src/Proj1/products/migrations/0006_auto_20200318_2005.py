# Generated by Django 3.0.4 on 2020-03-19 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200318_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
