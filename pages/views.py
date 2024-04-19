from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page(request):
    return HttpResponse("Anasayfa")

def contact_page(request):
    return HttpResponse("İletişim")

def about_page(request):
    return HttpResponse("Hakkımızda")