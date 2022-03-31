from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name = 'projects'),
    path('project/<str:pk>', views.project, name = 'project'),
    path('createform', views.create_proj, name = 'createform'),
    path('updateform/<str:pk>', views.update_proj, name='updateproject'),
    path('deleteform/<str:pk>', views.delete_proj, name='deleteproject')
]