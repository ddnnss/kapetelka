# Generated by Django 3.0.9 on 2020-10-22 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20201020_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Производитель')),
            ],
            options={
                'verbose_name': 'Производитель',
                'verbose_name_plural': 'Производители',
            },
        ),
        migrations.CreateModel(
            name='SampleExpirementField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('expiriment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.SampleExpirement')),
            ],
        ),
    ]
