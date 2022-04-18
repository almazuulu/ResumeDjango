from .models import *
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginateProject(request, all_projects, results):
    page = request.GET.get('page')
    paginator = Paginator(all_projects, results)

    try:
        all_projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        all_projects = paginator.page(page)
    except EmptyPage:
        # return redirect('projects')
        page = paginator.num_pages
        all_projects = paginator.page(page)

    leftindex = (int(page) - 2)

    if leftindex < 1:
        leftindex = 1

    rightindex = (int(page) + 2)

    if rightindex > paginator.num_pages:
        rightindex = paginator.num_pages + 1

    custom_range = range(leftindex, rightindex)

    return custom_range, all_projects

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