from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import *
from django import template
from django.template.loader import get_template
from pages.models import Ogrenci,Ders,Kullanici,Iletisim,Yorum,Urunn,Sepet
from django.template import loader
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password

def anasayfa(request):
   Giris=request.session.get('kullanici_adi', None)
   rol=request.session.get('rol',None)
   return render(request, 'anasayfa.html', {'Giris': Giris,'rol':rol})

def shop(request):
   Giris = request.session.get('kullanici_adi', None)
   rol = request.session.get('rol', None)
   site = "shop"
   urun = Urunn.objects.all()
   return render(request, 'shop/shop.html', {'Giris': Giris, 'rol': rol, 'urun': urun, 'site': site})

def shop2(request):
   Giris=request.session.get('kullanici_adi', None)
   rol=request.session.get('rol',None)
   errors=""
   urunn=Urunn.objects.all()
   ad=request.session.get('kullanici_adi', None)
   kullanici = Kullanici.objects.get(kullanici_adi=ad)
   if request.method == "POST":
      urun = request.POST['urun_ad']
      fiyat = request.POST['fiyat']
      adet=request.POST['adet']
      resim=request.FILES['resim']
      for add in urunn :
         if urun== add.adi:
            errors="Bu adda ayakkabı var"
            return render(request, 'shop/urun_ekle.html',{'kullanici':kullanici,'Giris': Giris,'rol':rol,'errors':errors})
      urunn = Urunn(adi=urun,adet=adet,fiyat=fiyat,resim=resim )      
      urunn.save() 
      return redirect('/shop')    
      
   return render(request, 'shop/urun_ekle.html',{'kullanici':kullanici,'errors':errors,'Giris': Giris,'rol':rol})

def kontrol(request):
   site="kontrol"
   kullanicilar = Kullanici.objects.all()
   Giris=request.session.get('kullanici_adi', None)
   rol=request.session.get('rol',None)
   urunn=Urunn.objects.all()
   return render(request, 'kontrol.html', {'Giris': Giris,'rol':rol,'kullanicilar':kullanicilar,'site':site,'urun':urunn})

def kullanici_guncelle(request):
   site="kontrol"
   kullanicilar = Kullanici.objects.all()
   Giris=request.session.get('kullanici_adi', None)
   rol=request.session.get('rol',None)
   urunn=Urunn.objects.all()
   if request.method == "POST":
      roll=request.POST['roll']
      ad=request.POST['adi']
      mail=request.POST['mail']
      tel=request.POST['tel']
      adres=request.POST['adres']
      yas=request.POST['yas']
      il=request.POST['il']
      isi=request.POST['isi']
      hak=request.POST['hak']
      guncel = Kullanici.objects.get(kullanici_adi=ad)
      guncel.kullanici_adi=ad
      guncel.eposta=mail
      guncel.telefon=tel
      guncel.adres=adres
      guncel.yas=yas
      guncel.il=il
      guncel.isi=isi
      guncel.hak=hak
      if roll=='yönetici' or roll=='yonetici' or roll=='Yönetici' or roll=='Yonetici':
         guncel.rol="yönetici"
      else:
         guncel.rol="standart"
      guncel.save()
      return render(request, 'kontrol.html', {'Giris': Giris,'rol':rol,'kullanicilar':kullanicilar,'site':site,'urun':urunn}) 
   
def urun_guncelle(request,x):
   gun=""
   site="kontrol"
   kullanicilar = Kullanici.objects.all()
   urunn=Urunn.objects.all()
   Giris=request.session.get('kullanici_adi', None)
   rol=request.session.get('rol',None)
   if request.method == "POST":
      ad=request.POST['ad']
      adet=request.POST['adet']
      fiyat=request.POST['fiyat']
      gun = Urunn.objects.get(id=x)
      gun.adi=ad
      gun.adet=adet
      gun.fiyat=fiyat
      gun.save()
      return render(request, 'kontrol.html', {'Giris': Giris,'rol':rol,'kullanicilar':kullanicilar,'site':site,'urun':urunn}) 

def sayfa1(request):
    
    ad = request.session.get('kullanici_adi', None)
    rol=request.session.get('rol',None)
    kullanici_ad = Kullanici.objects.all()
    yorumlar = Yorum.objects.all()
    site = "eyfel"

    if request.method == "POST":
        a = yorum(request, site)
        if a == 1:
            return redirect('/login')
        else:
            return render(request, 'siteler/eyfel.html', {'Giris': ad,'rol':rol, 'kullanici': kullanici_ad, 'yorumlar': yorumlar,'site':site})
    else:
        return render(request, 'siteler/eyfel.html', {'Giris': ad,'rol':rol, 'kullanici': kullanici_ad, 'yorumlar': yorumlar,'site':site})

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
    rol=request.session.get('rol',None)
    ad = request.session.get('kullanici_adi', None)
    kullanici_ad = Kullanici.objects.all()
    yorumlar = Yorum.objects.all()
    site = "cin-seddi"

    if request.method == "POST":
        a = yorum(request, site)
        if a == 1:
            return redirect('/login')
        else:
            return render(request, 'siteler/cin.html', {'Giris': ad,'rol':rol, 'kullanici': kullanici_ad, 'yorumlar': yorumlar,'site':site})
    else:
        return render(request, 'siteler/cin.html', {'Giris': ad,'rol':rol, 'kullanici': kullanici_ad, 'yorumlar': yorumlar,'site':site})

def cik(request):
   request.session['kullanici_adi'] =None
   request.session['rol'] =None
   return redirect('/')

def sayfa3(request):
    ad = request.session.get('kullanici_adi', None)
    rol=request.session.get('rol',None)
    kullanici_ad = Kullanici.objects.all()
    yorumlar = Yorum.objects.all()
    site = "rodos-heykeli"

    if request.method == "POST":
        a = yorum(request, site)
        if a == 1:
            return redirect('/login')
        else:
            return render(request, 'siteler/rodos.html', {'Giris': ad,'rol':rol, 'kullanici': kullanici_ad, 'yorumlar': yorumlar,'site':site})
    else:
        return render(request, 'siteler/rodos.html', {'Giris': ad,'rol':rol, 'kullanici': kullanici_ad, 'yorumlar': yorumlar,'site':site})
  
def sayfa4(request):
    ad = request.session.get('kullanici_adi', None)
    rol=request.session.get('rol',None)
    kullanici_ad = Kullanici.objects.all()
    yorumlar = Yorum.objects.all()
    site = "machu-picchu"

    if request.method == "POST":
        a = yorum(request, site)
        if a == 1:
            return redirect('/login')
        else:
            return render(request, 'siteler/machu.html', {'Giris': ad,'rol':rol, 'kullanici': kullanici_ad, 'yorumlar': yorumlar,'site':site})
    else:
        return render(request, 'siteler/machu.html', {'Giris': ad,'rol':rol, 'kullanici': kullanici_ad, 'yorumlar': yorumlar,'site':site})
  
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
    rol=request.session.get('rol',None)
    kullanici_ad = Kullanici.objects.all()
    yorumlar = Yorum.objects.all()
    site = "tac-mahal"

    if request.method == "POST":
        a = yorum(request, site)
        if a == 1:
            return redirect('/login')
        else:
            return render(request, 'siteler/tacmahal.html', {'Giris': ad,'rol':rol, 'kullanici': kullanici_ad, 'yorumlar': yorumlar,'site':site})
    else:
        return render(request, 'siteler/tacmahal.html', {'Giris': ad,'rol':rol, 'kullanici': kullanici_ad, 'yorumlar': yorumlar,'site':site})
  
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
                request.session['rol'] = kullanici2.rol
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
      rol=request.POST['rol']
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
         if rol=='yönetici' or rol=='yonetici' or rol=='Yönetici' or rol=='Yonetici':
            kullanici_ekle.rol="yönetici"
         else:
            kullanici_ekle.rol="standart"
            
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
   rol=request.session.get('rol',None)
   ad=request.session.get('kullanici_adi', None)
   errors=""
   try:
         # Kullanıcıyı veritabanında adına göre getirin
         kullanici = Kullanici.objects.get(kullanici_adi=ad)
         return render(request, 'siteler/profil.html',{'kullanici': kullanici,'Giris': ad,"rol":rol})   
   except Kullanici.DoesNotExist:
            # Kullanıcı adı bulunamazsa hata mesajı gösterin
            errors = "Giriş Yapın"
            return render(request, 'siteler/profil.html',{'errors': errors,"Giris":ad,"rol":rol})
         
def delete_comment(request, x,site):
    comment_id=x
    site="/"+site
    try:
        comment = Yorum.objects.get(id=comment_id)
        comment.delete()
    except Yorum.DoesNotExist:
        pass
    return redirect(site)
 
def delete_user(request, site,x):
    comment_id=x
    site="/"+site
    try:
        comment = Kullanici.objects.get(id=comment_id)
        comment.delete()
    except Kullanici.DoesNotExist:
        pass
    return redirect(site)
 
def sepet(request, x,site):
   site="/"+site
   adet = int(request.POST['adett'])
   if adet>0:
      urunnn = Urunn.objects.get(id=x)
      fiyat = int(urunnn.fiyat)
      toplam = adet * fiyat
      sepe=Sepet.objects.filter(adi=urunnn.adi,onay=0).first()
      if not sepe:
         sepet=Sepet(adi=urunnn.adi,resim=urunnn.resim,fiyat=urunnn.fiyat,adet=adet,toplam=toplam,onay=0)
         sepet.save()
      else:
            sepe.adet += adet
            sepe.toplam=sepe.fiyat*sepe.adet
            sepe.save()
            return redirect(site)
     
   return redirect(site)

def sepet_cikar(request, x,site):
   adet = int(request.POST['adett'])
   sep = Sepet.objects.get(id=x,onay=0)
   kalan=sep.adet+adet
   toplam =sep.fiyat*kalan
   site="/"+site
   if kalan==0:
      sep.delete()
      return redirect(site)
   sep.adet=kalan
   sep.toplam=toplam
   sep.onay=0
   sep.save()
   return redirect(site)
  
def sepett(request):
   site="sepetin"
   toplam=0
   Giris=request.session.get('kullanici_adi', None)
   rol=request.session.get('rol',None)
   sepet= Sepet.objects.filter(onay=0)
   for x in sepet:
      toplam+=x.toplam
   return render(request, 'shop/sepet.html', {'Giris': Giris,'rol':rol,"sepet":sepet,"site":site,"toplam":toplam})

def satin(request,site):
   site="/"+site
   Giris=request.session.get('kullanici_adi', None)
   if Giris==None:
      sit="/giris"
      return redirect(sit)
   else:
      sepet= Sepet.objects.filter(onay=0)
      for x in sepet:
         x.alan=Giris
         x.onay=1
         x.save()
      return redirect(site)