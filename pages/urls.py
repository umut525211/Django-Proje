from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib import admin
urlpatterns = [
    path('', views.anasayfa),
    path('giris', views.index),
    path('kayit', views.kayit),
    path('log', views.log),
    path('ogrenci/', views.ogrenci),
    path('ogrenci-liste', views.ogrenci_listesi),
    path('index', views.anasayfa),
    path('iletisim',views.iletisim),
    path('hakkimizda',views.hakkimizda)
]
