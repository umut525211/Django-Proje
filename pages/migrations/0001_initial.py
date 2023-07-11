# Generated by Django 4.2.3 on 2023-07-07 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ogrenci',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=30)),
                ('soyad', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Ders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=100)),
                ('ogrenciler', models.ManyToManyField(to='pages.ogrenci')),
            ],
        ),
    ]