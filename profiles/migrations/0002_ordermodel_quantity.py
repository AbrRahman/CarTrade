# Generated by Django 5.0 on 2024-01-04 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]
