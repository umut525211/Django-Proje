from django.db import models
import datetime,os
from django.contrib.auth.hashers import make_password

class Ogrenci(models.Model):
    ad = models.CharField(max_length=30)
    soyad = models.CharField(max_length=30)
    telefon=models.IntegerField(null=True)
class Ders(models.Model):
    ad = models.CharField(max_length=100)
    ogrenciler = models.ManyToManyField(Ogrenci)
    
def resim(instance, filename):
    kullanici_adi = instance.kullanici_adi
    user_directory = os.path.join('static/resimler', kullanici_adi)
    return os.path.join(user_directory, filename)

def resim2(instance, filename): 
    adi = instance.adi
    user_directory = os.path.join('static/urunler', adi)
    return os.path.join(user_directory, filename)

class Iletisim(models.Model):
    kullanici=models.CharField(max_length=100)
    tur=models.CharField(max_length=40)
    mesaj=models.CharField(max_length=6000)
    
class Yorum(models.Model):
    kullanici=models.CharField(max_length=100)
    site=models.CharField(max_length=50)
    yorum=models.CharField(max_length=3000)
    
class Urunn(models.Model):
    adi=models.CharField(max_length=100)
    resim=models.ImageField(upload_to=resim2, null=True)
    adet=models.IntegerField(null=True)
    fiyat=models.IntegerField(null=True)
    
class Sepet(models.Model):
    alan=models.CharField(max_length=1000,null=True)
    adi=models.CharField(max_length=100, null=False)
    resim=models.CharField(max_length=1000,null=False)
    fiyat=models.IntegerField(null=True)
    adet=models.IntegerField(null=False)
    toplam=models.IntegerField(null=False)
    onay=models.IntegerField(null=False)
    
      
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
    rol=models.CharField(max_length=200,null=True)
    resim=models.ImageField(upload_to=resim, null=True)
  
    def save2(self, *args, **kwargs):
        # Şifreleri otomatik olarak şifreli olarak kaydedin.
        self.sifre = make_password(self.sifre)
        super(Kullanici, self).save(*args, **kwargs)

    def __str__(self):
        return self.kullanici_adi




