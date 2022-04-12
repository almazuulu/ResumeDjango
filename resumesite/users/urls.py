from django.urls import path, include
from .views import *

urlpatterns = [
    path('', profiles, name = 'profiles'),
    path('profile/<str:pk>', profile, name = 'profile'),
    path('login/', loginPage, name = 'login'),
    path('logout/', logoutProfile, name='logout'),
    path('register/', registerUser, name='register' )

]
