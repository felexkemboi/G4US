# Generated by Django 2.0 on 2018-04-25 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebooks', '0008_auto_20180425_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(upload_to='media/'),
        ),
    ]