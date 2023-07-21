from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import *
from django import template
from django.template.loader import get_template
from pages.models import Ogrenci,Ders,Kullanici
from django.template import loader
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from django.template import loader

def anasayfa(request):
   Giris=request.session.get('kullanici_adi', None)
   return render(request, 'anasayfa.html', {'Giris': Giris})

def sayfa1(request):
   Giris=request.session.get('kullanici_adi', None)
   return render(request, 'siteler/eyfel.html', {'Giris': Giris})

def sayfa2(request):
   Giris=request.session.get('kullanici_adi', None)
   return render(request, 'siteler/cin.html', {'Giris': Giris})

def cik(request):
   request.session['kullanici_adi'] =None
   return redirect('/')

def sayfa3(request):
   Giris=request.session.get('kullanici_adi', None)
   return render(request, 'siteler/rodos.html', {'Giris': Giris})

def sayfa4(request):
   Giris=request.session.get('kullanici_adi', None)
   return render(request, 'siteler/machu.html', {'Giris': Giris})
   
def sayfa5(request):
   Giris=request.session.get('kullanici_adi', None)
   return render(request, 'siteler/tacmahal.html', {'Giris': Giris})

#def log2(request):
   #return render(request, 'log.html',{'resim':resim})
   kullanici_ad= Kullanici.objects.all()
   success=""
   errors=""
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

def log(request):
   #return render(request, 'log.html',{'resim':resim})
   kullanici_ad= Kullanici.objects.all()
   success=""
   errors=""
   if request.method == "POST":
      ad = request.POST['kullanici']
      sifre = request.POST['sifre']
      try:
            # Kullanıcıyı veritabanında adına göre getirin
            kullanici = Kullanici.objects.get(kullanici_adi=ad)
            
            # Girilen şifreyi doğrulayın
            if check_password(sifre, kullanici.sifre):
                # Şifre doğruysa oturum aç
                request.session['kullanici_id'] = kullanici.id
                request.session['kullanici_adi'] = kullanici.kullanici_adi
                return redirect('/')  # Kullanıcı başarıyla giriş yaptıysa, ana sayfaya yönlendirin.
            else:
                # Şifre yanlışsa hata mesajı gösterin
                errors = "Geçersiz şifre."
      except Kullanici.DoesNotExist:
            # Kullanıcı adı bulunamazsa hata mesajı gösterin
            errors = "Kullanıcı adı bulunamadı."
   else:
        errors = None
   return render(request, 'log.html', {'errors': errors})

def kayit(request):
   #return render(request, 'log.html',{'resim':resim})
   kullanici_ad= Kullanici.objects.all()
   errors=""
   if request.method == "POST":
      ad = request.POST['kullanici']
      sifre = request.POST['sifre']
      mail=request.POST['mail']
      for kullanici in kullanici_ad:
         if ad== kullanici.kullanici_adi:
            errors="Bu kullanıcı adı kullanılıyor"
            return render(request,'kayit.html',{'errors':errors})
         if mail==kullanici.eposta:
            errors="Bu mail adresi kullanılıyor"
            return render(request, 'kayit.html',{'errors':errors})
      if len(ad)>0:
         kullanici_ekle=Kullanici(kullanici_adi=ad,eposta=mail,sifre=sifre)
         kullanici_ekle.save() 
         return redirect('/')    
   
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