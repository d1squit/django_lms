from django.urls import path

from teachers.views import *


app_name = 'teachers'

urlpatterns = [
    path('', get_teachers, name='list'),
    path('update/<int:pk>/', update_teacher, name='update'),
    path('detail/<int:pk>/', detail_teacher, name='detail')
]
