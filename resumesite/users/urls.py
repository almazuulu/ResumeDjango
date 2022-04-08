from django.urls import path, include
from .views import *

urlpatterns = [
    path('', profiles, name = 'profiles'),
    path('profile/<str:pk>', profile, name = 'profile')

]
