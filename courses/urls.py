from django.urls import path
from . import views
urlpatterns = [
    path('list', views.course_list),
    path('details', views.detail),
    path('<category>', views.get_course_by_category)
]
