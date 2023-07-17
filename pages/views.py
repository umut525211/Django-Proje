from django.http import HttpResponse
from django.shortcuts import render
from django.http import *
from django import template
from django.template.loader import get_template
from pages.models import Ogrenci,Ders,Kullanici
from django.template import loader
def anasayfa(request):
 return render(request, 'anasayfa.html')
   
def log(request):
   resim="images/wallpaperbetter.jpg"
   #return render(request, 'log.html',{'resim':resim})
   kullanici_ad= Kullanici.objects.all()
   success=""
   errors=[]
   if request.method == "POST":
      ad = request.POST['kullanici']
      sifre = request.POST['sifre']
      for kullanici in kullanici_ad:
         if ad== kullanici.kullanici_adi:
            if sifre==kullanici.sifre:
               success="*Giriş Başarılı"
               return render(request,'log.html',{'success':success})

         else:
            errors="Kullanıcı Adı ya da Şifre Yanlış"
   
   return render(request, 'log.html',{'errors': errors})

def kayit(request):
   #return render(request, 'log.html',{'resim':resim})
   kullanici_ad= Kullanici.objects.all()
   
   errors=[]
   if request.method == "POST":
      ad = request.POST['kullanici']
      sifre = request.POST['sifre']
      mail=request.POST['mail']
      for kullanici in kullanici_ad:
         if ad== kullanici.kullanici_adi:
            if sifre==kullanici.sifre:
               return render(request,'log.html',{'success':True})
         if mail==kullanici.eposta:
            errors="Bu mail adresi kullanılıyor"
            return render(request, 'log.html',{'errors':errors})
      if len(ad)>0:
         kullanici_ekle=Kullanici(kullanici_adi=ad,eposta=mail,sifre=sifre)
         kullanici_ekle.save() 
         return render(request, 'anasayfa.html')    
   
   return render(request, 'kayit.html',{'errors': errors})

def index(request):
  error=False
  if 'isim' in request.POST:
     isim = request.POST['isim']
     if not isim:
        error=True
     else:
        return HttpResponse('Merhaba %s'%isim)
  return render(request, 'index.html', {'error': error})

def iletisim(request):
    return HttpResponse('iletisim')

def hakkimizda(request):
    return HttpResponse("hakkimizda")

def ogrenci(request):
   errors=[]
   if request.method == "POST":
      ad = request.POST['ad']
      soyad = request.POST['soyad']
      if not ad:
         errors.append("Lütfen bir ad giriniz.")
      if not soyad:
         errors.append("Lütfen bir soyad giriniz.")
      if errors:
         return render(request, 'ogrenci.html', {'errors': errors})
      else:
         ogrenci=Ogrenci(ad=ad,soyad=soyad)
         ogrenci.save()
      return render(request, 'ogrenci.html', {'success': True})
   return render(request, 'ogrenci.html', {'errors': errors})

def ogrenci_listesi(request):
   ogrenci_listesi = Ogrenci.objects.all()
   t = loader.get_template('ogrenciler.html')
   context = {'ogrenci_list': ogrenci_listesi}
   html = t.render(context, request)
   return HttpResponse(html)