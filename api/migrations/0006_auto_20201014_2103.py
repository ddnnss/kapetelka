# Generated by Django 3.0.9 on 2020-10-14 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20201014_2102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='text',
        ),
        migrations.RemoveField(
            model_name='category',
            name='value',
        ),
    ]