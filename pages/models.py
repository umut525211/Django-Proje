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
    # Assuming 'kullanici_adi' is a field in the model containing the user's username
    kullanici_adi = instance.kullanici_adi
    # Create a directory path using the user's username
    user_directory = os.path.join('static/resimler', kullanici_adi)
    # Return the full upload path (relative to 'MEDIA_ROOT') including the original filename
    return os.path.join(user_directory, filename)

class Iletisim(models.Model):
    kullanici=models.CharField(max_length=100)
    tur=models.CharField(max_length=40)
    mesaj=models.CharField(max_length=6000)
    
class Yorum(models.Model):
    kullanici=models.CharField(max_length=100)
    site=models.CharField(max_length=50)
    yorum=models.CharField(max_length=3000)
       
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
    resim=models.ImageField(upload_to=resim, null=True)
  
    def save2(self, *args, **kwargs):
        # Şifreleri otomatik olarak şifreli olarak kaydedin.
        self.sifre = make_password(self.sifre)
        super(Kullanici, self).save(*args, **kwargs)

    def __str__(self):
        return self.kullanici_adi




