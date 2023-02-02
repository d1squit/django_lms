from django.contrib import admin
from django.urls import path

from students.views import index, get_students, create_student

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('students/', get_students),
    path('students/create', create_student)
]
