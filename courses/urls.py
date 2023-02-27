from django.urls import path

from courses.views import *


app_name = 'courses'

urlpatterns = [
    path('', get_courses, name='list'),
    path('create/', create_course, name='create'),
    path('update/<int:pk>/', update_course, name='update'),
    path('detail/<int:pk>/', detail_course, name='detail'),
    path('delete/<int:pk>/', delete_course, name='delete')
]
