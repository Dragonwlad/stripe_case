# Generated by Django 4.2.8 on 2023-12-26 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.CharField(max_length=50),
        ),
    ]