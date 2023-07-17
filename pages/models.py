from django.db import models
class Ogrenci(models.Model):
    ad = models.CharField(max_length=30)
    soyad = models.CharField(max_length=30)
    telefon=models.IntegerField(null=True)
class Ders(models.Model):
    ad = models.CharField(max_length=100)
    ogrenciler = models.ManyToManyField(Ogrenci)
    
class Kullanici(models.Model):
    kullanici_adi=models.CharField(max_length=30)
    eposta=models.CharField(max_length=30)
    sifre=models.CharField(max_length=15)

