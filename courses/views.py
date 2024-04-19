from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def course_list(request):
    return HttpResponse('Kurs Listesi')

def detail(request):
    return HttpResponse('Kurs Detay Sayfasi')

def programming_list(request):
    return HttpResponse('Programlama Kursları Listesi')

def mobile_app_list(request):
    return HttpResponse('Mobil Uygulama Kursları Listesi')