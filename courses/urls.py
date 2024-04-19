from django.urls import path
from . import views
urlpatterns = [
    path('list', views.course_list),
    path('programming', views.programming_list),
    path('mobile-app', views.mobile_app_list),
    path('details', views.detail)
]
