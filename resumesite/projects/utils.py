from .models import *
from django.db.models import Q

def search_project(request):
    search_query = ''
    tag = Tag.objects.filter(name__icontains = search_query)
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    all_projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(owner__name__icontains=search_query) |
        Q(tags__in = tag)
    )

    return all_projects, search_query