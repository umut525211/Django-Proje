from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from django.template.loader import get_template
data = {
    "programlama": "Programlama kategorisi",
    "web-gelistirme": "Web geliştirme",
    "mobil": "Mobil"
}

def kurslar(request):
    list_items = ""
    category_list = list(data.keys())

    for category in category_list:
        redirect_url = reverse("courses_by_category", args=[category])
        list_items += f"<li><a href='{redirect_url}'>{category}</a></li>"

    html = f"<h1>Kurs Listesi</h1><br><ul>{list_items}</ul>"

    return HttpResponse(html)

def courses_by_category(request, category):
    # Kategoriye göre ilgili kursları işleyen kodu burada yazınız
    pass

def details(request,kurs_adi):
    return HttpResponse(f"{kurs_adi} kursu detay sayfası")

def getCourseByCategory(request,category_name):
    text=""
    if(category_name=="programlama"):
        text=f"{category_name} kategorisindeki kurs listesi"
    elif(category_name=="web-geliştirme"):
        text=f"{category_name} kategorisindeki kurs listesi"
    else:
        text="Yanlış kategori seçimi"
    return HttpResponse(text)
def getCourseByCategoryId(request,category_id):
    return HttpResponse(category_id)
    #return redirect('/kurs/programlama')
# HttpResponseRedirect sonuç olarak url ye veri ekliyor