# Generated by Django 3.0.4 on 2020-03-26 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200325_2308'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-pk']},
        ),
    ]
