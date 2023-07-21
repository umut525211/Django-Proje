from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib import admin
urlpatterns = [
    path('', views.anasayfa),
    path('anasayfa', views.anasayfa),
    path('home', views.anasayfa),
    path('eyfel', views.sayfa1),
    path('cin-seddi', views.sayfa2),
    path('rodos-heykeli', views.sayfa3),
    path('machu-picchu', views.sayfa4),
    path('tac-mahal', views.sayfa5),
    path('bilgi', views.bilgi),
    path('profil', views.profil),
    path('çıkış', views.cik),
    path('giris', views.log),
    path('kayit', views.kayit),
    path('login', views.log),
    path('ogrenci/', views.ogrenci),
    path('ogrenci-liste', views.ogrenci_listesi),
    path('index', views.anasayfa),
]
