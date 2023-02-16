from django.contrib import admin
from django.urls import path, include

from students.views import *
from groups.views import *
from teachers.views import *
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', index, name='home'),
    path('students/', include('students.urls')),
    path('groups/', include('groups.urls')),
    path('teachers/', include('teachers.urls')),
]
