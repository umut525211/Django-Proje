# Generated by Django 4.2.3 on 2023-08-01 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_sepet_alan'),
    ]

    operations = [
        migrations.AddField(
            model_name='sepet',
            name='fiyat',
            field=models.IntegerField(null=True),
        ),
    ]
