from django.urls import path
from . import views
from django.contrib import admin
urlpatterns = [
    path('', views.anasayfa),
    path('giris', views.index),
    path('ogrenci/', views.ogrenci),
    path('ogrenci-liste', views.ogrenci_listesi),
    path('index', views.anasayfa),
    path('iletisim',views.iletisim),
    path('hakkimizda',views.hakkimizda)
]