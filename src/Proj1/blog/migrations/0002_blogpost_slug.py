# Generated by Django 3.0.4 on 2020-03-24 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(default='ww-ww'),
            preserve_default=False,
        ),
    ]
