# Generated by Django 2.0 on 2018-04-25 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ebooks', '0002_auto_20180425_1154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='created_at',
            new_name='created_date',
        ),
    ]