# Generated by Django 4.2.3 on 2023-07-21 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kullanici',
            name='adres',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='kullanici',
            name='il',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='kullanici',
            name='telefon',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='kullanici',
            name='yas',
            field=models.CharField(max_length=5, null=True),
        ),
    ]