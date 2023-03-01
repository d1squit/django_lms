from django.urls import path

from teachers.views import *


app_name = 'teachers'

urlpatterns = [
    path('', ListTeacherView.as_view(), name='list'),
    path('create/', CreateTeacherView.as_view(), name='create'),
    path('update/<int:pk>/', UpdateTeacherView.as_view(), name='update'),
    path('detail/<int:pk>/', DetailTeacherView.as_view(), name='detail'),
    path('delete/<int:pk>/', DeleteTeacherView.as_view(), name='delete')
]
