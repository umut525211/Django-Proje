from django.http import HttpResponse
from django.shortcuts import render
from django.http import *
from django import template
from django.template.loader import get_template
from pages.models import Ogrenci,Ders
from django.template import loader
def anasayfa(request):
 return render(request, 'anasayfa.html')

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