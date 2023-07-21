from django.db import models
from django.contrib.auth.hashers import make_password
class Ogrenci(models.Model):
    ad = models.CharField(max_length=30)
    soyad = models.CharField(max_length=30)
    telefon=models.IntegerField(null=True)
class Ders(models.Model):
    ad = models.CharField(max_length=100)
    ogrenciler = models.ManyToManyField(Ogrenci)
    
class Kullanici(models.Model):
    kullanici_adi=models.CharField(max_length=100)
    eposta=models.CharField(max_length=30)
    sifre=models.CharField(max_length=128)
    telefon=models.CharField(max_length=50,null=True)
    adres=models.CharField(max_length=300,null=True)
    yas=models.CharField(max_length=5,null=True)
    il=models.CharField(max_length=20,null=True)
    isi=models.CharField(max_length=30,null=True)
    hak=models.CharField(max_length=200,null=True)
    
    
    def save(self, *args, **kwargs):
        # Şifreleri otomatik olarak şifreli olarak kaydedin.
        self.sifre = make_password(self.sifre)
        super(Kullanici, self).save(*args, **kwargs)

    def __str__(self):
        return self.kullanici_adi




