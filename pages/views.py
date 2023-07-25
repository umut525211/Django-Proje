from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import *
from django import template
from django.template.loader import get_template
from pages.models import Ogrenci,Ders,Kullanici,Iletisim,Yorum
from django.template import loader
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from django.template import loader

def anasayfa(request):
   Giris=request.session.get('kullanici_adi', None)
   return render(request, 'anasayfa.html', {'Giris': Giris})

def sayfa1(request):
    ad = request.session.get('kullanici_adi', None)
    kullanici_ad = Kullanici.objects.all()
    yorumlar = Yorum.objects.all()
    site = "eyfel"

    if request.method == "POST":
        a = yorum(request, site)
        if a == 1:
            return redirect('/login')
        else:
            return render(request, 'siteler/eyfel.html', {'Giris': ad, 'kullanici': kullanici_ad, 'yorumlar': yorumlar,'site':site})
    else:
        return render(request, 'siteler/eyfel.html', {'Giris': ad, 'kullanici': kullanici_ad, 'yorumlar': yorumlar,'site':site})

def yorum(request, site):
    ad = request.session.get('kullanici_adi', None)

    if ad is None:
        return 1
    else:
        yorum_text = request.POST['yorum']
        yorum1 = Yorum(kullanici=ad, site=site, yorum=yorum_text)
        yorum1.save()
        return 0

def sayfa2(request):
    ad = request.session.get('kullanici_adi', None)
    kullanici_ad = Kullanici.objects.all()
    yorumlar = Yorum.objects.all()
    site = "cin"

    if request.method == "POST":
        a = yorum(request, site)
        if a == 1:
            return redirect('/login')
        else:
            return render(request, 'siteler/cin.html', {'Giris': ad, 'kullanici': kullanici_ad, 'yorumlar': yorumlar})
    else:
        return render(request, 'siteler/cin.html', {'Giris': ad, 'kullanici': kullanici_ad, 'yorumlar': yorumlar})

def cik(request):
   request.session['kullanici_adi'] =None
   return redirect('/')

def sayfa3(request):
    ad = request.session.get('kullanici_adi', None)
    kullanici_ad = Kullanici.objects.all()
    yorumlar = Yorum.objects.all()
    site = "rodos"

    if request.method == "POST":
        a = yorum(request, site)
        if a == 1:
            return redirect('/login')
        else:
            return render(request, 'siteler/rodos.html', {'Giris': ad, 'kullanici': kullanici_ad, 'yorumlar': yorumlar,'site':site})
    else:
        return render(request, 'siteler/rodos.html', {'Giris': ad, 'kullanici': kullanici_ad, 'yorumlar': yorumlar,'site':site})
  
def sayfa4(request):
    ad = request.session.get('kullanici_adi', None)
    kullanici_ad = Kullanici.objects.all()
    yorumlar = Yorum.objects.all()
    site = "machu"

    if request.method == "POST":
        a = yorum(request, site)
        if a == 1:
            return redirect('/login')
        else:
            return render(request, 'siteler/machu.html', {'Giris': ad, 'kullanici': kullanici_ad, 'yorumlar': yorumlar,'site':site})
    else:
        return render(request, 'siteler/machu.html', {'Giris': ad, 'kullanici': kullanici_ad, 'yorumlar': yorumlar,'site':site})
  
def iletisim(request):
   ad=request.session.get('kullanici_adi', None)
   kullanici_ad= Kullanici.objects.all()
   errors=""
   success=""
   if request.method == "POST":
      mesaj_tur = request.POST['istek']
      mesaj=request.POST['mesaj']
      
      if ad==None:
            errors="Giriş Yapmalısınız"
            return render(request,'iletisim.html',{'errors':errors,'Giris': ad})
      if ad!=None:
         message=Iletisim()
         message.kullanici=ad
         message.tur=mesaj_tur
         message.mesaj=mesaj
         message.save()
         success="Mesajınız Gönderildi"
         return render(request, 'iletisim.html',{'success': success,'Giris': ad})
   return render(request, 'iletisim.html',{'errors':errors,'Giris': ad})

def sayfa5(request):
    ad = request.session.get('kullanici_adi', None)
    kullanici_ad = Kullanici.objects.all()
    yorumlar = Yorum.objects.all()
    site = "tac"

    if request.method == "POST":
        a = yorum(request, site)
        if a == 1:
            return redirect('/login')
        else:
            return render(request, 'siteler/tacmahal.html', {'Giris': ad, 'kullanici': kullanici_ad, 'yorumlar': yorumlar,'site':site})
    else:
        return render(request, 'siteler/tacmahal.html', {'Giris': ad, 'kullanici': kullanici_ad, 'yorumlar': yorumlar,'site':site})
  
def log(request):
   #return render(request, 'log.html',{'resim':resim})
   errors=""
   if request.method == "POST":
      ad = request.POST['kullanici']
      sifre = request.POST['sifre']
      try:
            # Kullanıcıyı veritabanında adına göre getirin
            kullanici2 = Kullanici.objects.get(kullanici_adi=ad)
            
            # Girilen şifreyi doğrulayın
            if check_password(sifre, kullanici2.sifre):
                # Şifre doğruysa oturum aç
                request.session['kullanici_id'] = kullanici2.id
                request.session['kullanici_adi'] = kullanici2.kullanici_adi
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
         kullanici_ekle.adres=""
         kullanici_ekle.telefon=""
         kullanici_ekle.yas=""
         kullanici_ekle.il=""
         kullanici_ekle.isi=""
         kullanici_ekle.hak=""
         kullanici_ekle.resim="static/images/1.jpg"
         kullanici_ekle.save2() 
         return redirect('/')    
   
   return render(request, 'kayit.html',{'errors': errors})

def bilgi(request):
   ad=request.session.get('kullanici_adi', None)
   kullanici = Kullanici.objects.get(kullanici_adi=ad)
   #return render(request, 'log.html',{'resim':resim})s
   errors=""
   if request.method == "POST":
      tel = request.POST['telefon']
      adres = request.POST['adres']
      yas=request.POST['yas']
      il=request.POST['il']
      isi=request.POST['is']
      hak=request.POST['hak']
      try:
            # Kullanıcıyı veritabanında adına göre getirin
            kullanici = Kullanici.objects.get(kullanici_adi=ad)
            kullanici.sifre
            kullanici.adres=adres
            kullanici.telefon=tel
            kullanici.yas=yas
            kullanici.il=il
            kullanici.isi=isi
            kullanici.hak=hak
            
            if len(request.FILES)!=0:
               kullanici.resim=request.FILES['resim']
               
            kullanici.save() 
            return redirect('/')    
      except Kullanici.DoesNotExist:
            # Kullanıcı adı bulunamazsa hata mesajı gösterin
            errors = "Giriş Yapın"
   return render(request, 'siteler/bilgi.html',{'kullanici':kullanici,'errors': errors})

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

def profil(request):
   ad=request.session.get('kullanici_adi', None)
   errors=""
   try:
         # Kullanıcıyı veritabanında adına göre getirin
         kullanici = Kullanici.objects.get(kullanici_adi=ad)
         return render(request, 'siteler/profil.html',{'kullanici': kullanici,'Giris': ad})   
   except Kullanici.DoesNotExist:
            # Kullanıcı adı bulunamazsa hata mesajı gösterin
            errors = "Giriş Yapın"
            return render(request, 'siteler/profil.html',{'errors': errors})