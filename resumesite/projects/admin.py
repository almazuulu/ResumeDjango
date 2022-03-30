from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Project)
# admin.site.register(Review)
# admin.site.register(Tag)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('project', 'body')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')




