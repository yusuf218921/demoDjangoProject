from django.urls import path
from . import views
urlpatterns = [
    path('list', views.course_list),
    path('<str:course_name>', views.detail),
    path('category/<int:category_id>', views.get_course_by_category_id),
    path('category/<str:category_name>', views.get_course_by_category_name)
]
