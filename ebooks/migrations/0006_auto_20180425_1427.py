# Generated by Django 2.0 on 2018-04-25 11:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ebooks', '0005_auto_20180425_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
