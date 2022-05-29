from django.urls import path, include
from .views import *

urlpatterns = [
    path('', getRoutes,),
    path('projects/', getProjects),
    path('projects/<str:pk>', getProject),

]