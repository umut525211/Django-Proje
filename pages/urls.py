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
    path('iletisim', views.iletisim),
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
    path('kontrol', views.kontrol),
    path('shop/', views.shop),
    path('urun_ekle', views.shop2),
    path('sepetin', views.sepett),
    path('kullanici_guncelle/', views.kullanici_guncelle, name='kullanici_guncelle'),
    path('urun_guncelle/<int:x>', views.urun_guncelle, name='urun_guncelle'),
    path('delete_comment/<int:x>/<str:site>', views.delete_comment, name='delete_comment'),
    path('sepet/<int:x>/<str:site>', views.sepet, name='sepet'),
    path('sepet_cikar/<int:x>/<str:site>', views.sepet_cikar, name='sepet_cikar'),
    path('delete_user/<str:site>/<int:x>', views.delete_user, name='delete_user'),
]
