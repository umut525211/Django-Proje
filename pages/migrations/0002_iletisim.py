# Generated by Django 4.2.3 on 2023-07-24 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Iletisim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kullanici', models.CharField(max_length=100)),
                ('tur', models.CharField(max_length=40)),
                ('mesaj', models.CharField(max_length=6000)),
            ],
        ),
    ]
