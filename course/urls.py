from django.urls import path
from . import views

urlpatterns = [
    path('<str:category_name>/', views.getCourseByCategory),
    path('<str:category>/', views.courses_by_category, name='courses_by_category'),
    path('',views.kurslar),
    path('list', views.kurslar,name='courses_by_category'),
    path('details/<kurs_adi>', views.details),
    path('<int:category_id>', views.getCourseByCategoryId),

]

