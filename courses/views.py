from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse

# Create your views here.

data = {
    'programlama' : 'Pragramlama Kurslarının Listesi',
    'web-gelistirme' : 'Web Gelistirme Kursları Listesi',
    'mobil' : 'Mobil Uygulama Gelistirme Kurslarının Listesi'
}

def course_list(request):
    return HttpResponse('Kurs Listesi')

def detail(request, course_name):
    return HttpResponse(f'{course_name} Kursu Detay Sayfasi')

def get_course_by_category_name(request, category_name):

    try:
        text = data[category_name]
        return HttpResponse(text)
    except:
        return HttpResponseNotFound("Geçersiz Kategori Girildi")

def get_course_by_category_id(request, category_id):
    category_list = list(data.keys())
    if (category_id > len(category_list)):
        return HttpResponseNotFound("Geçersiz Kategori Girildi")
    category_name = category_list[category_id - 1]
    redirect_text = reverse('courses_by_category_name', args=[category_name])
    return redirect(redirect_text)