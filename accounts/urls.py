from django.urls import path

from accounts.views import *


app_name = 'accounts'

urlpatterns = [
    path('register/', AccountRegisterView.as_view(), name='register'),
    path('login/', AccountLoginView.as_view(), name='login'),
    path('logout/', AccountLogoutView.as_view(), name='logout'),
    path('profile/', profile_view, name='profile'),
    path('profile/update/', UpdateProfileView.as_view(), name='profile_update'),
]
