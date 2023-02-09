from django.contrib import admin
from django.urls import path

from students.views import *
from groups.views import *
from teachers.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('students/', get_students),
    path('students/create/', create_student),
    path('students/update/<int:pk>/', update_student),
    path('students/detail/<int:pk>/', detail_student),
    path('groups/', get_groups),
    path('groups/detail/<int:pk>/', detail_group),
    path('groups/update/<int:pk>/', update_group),
    path('teachers/', get_teachers),
    path('teachers/detail/<int:pk>/', detail_teacher),
    path('teachers/update/<int:pk>/', update_teacher)
]
