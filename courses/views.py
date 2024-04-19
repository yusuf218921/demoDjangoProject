from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def course_list(request):
    return HttpResponse('Kurs Listesi')

def detail(request):
    return HttpResponse('Kurs Detay Sayfasi')

def get_course_by_category(request, category):
    text = ''

    if (category == 'programlama'):
        text = 'Pragramlama kurslarının Listesi'
    elif (category == 'web-gelistirme'):
        text = 'Web Gelistirme Kursları Listesi'
    else:
        text = 'Geçersiz kategori girildi'

    return HttpResponse(text)