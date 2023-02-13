from django.urls import path

from groups.views import *


app_name = 'groups'

urlpatterns = [
    path('', get_groups, name='list'),
    path('update/<int:pk>/', update_group, name='update'),
    path('detail/<int:pk>/', detail_group, name='detail')
]
