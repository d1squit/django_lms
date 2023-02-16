from django.urls import path

from teachers.views import *


app_name = 'teachers'

urlpatterns = [
    path('', get_teachers, name='list'),
    path('create/', create_teacher, name='create'),
    path('update/<int:pk>/', update_teacher, name='update'),
    path('detail/<int:pk>/', detail_teacher, name='detail'),
    path('delete/<int:pk>/', delete_teacher, name='delete')
]
