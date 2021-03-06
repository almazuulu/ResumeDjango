from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from .utils import search_project, paginateProject
from django.contrib import messages

from .models import *
from .forms import ProjectForm, ReviewForm

# Create your views here.

def projects(request):
    all_projects, search_query = search_project(request)
    results = 3

    custom_range, all_projects = paginateProject(request,all_projects, results)

    context = {
        'projectslist': all_projects,
        'search_query': search_query,
        'custom_range': custom_range
    }
    return render(request, 'projects/projects.html', context= context)

def project(request, pk):
    projectObj = Project.objects.get(id = pk)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner = request.user.profile
        review.save()

        messages.success(request, 'Комментарий успешно обновлен!')

        projectObj.getVotedCount

        redirect('project', pk=projectObj.id)

    context = {
        'project': projectObj,
        'form': form
    }

    return render(request, 'projects/single-project.html', context)

@login_required(login_url='login')
def create_proj(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)

        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()

            return redirect('projects')

    context = {
        "form": form
    }
    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def update_proj(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)

    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)

        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {
        "form": form
    }
    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def delete_proj(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {
        "object": project
    }
    return render(request, 'delete_form.html', context)

#def search_proj(request):
    # if request.method == 'GET':
    #     query = request.GET.get('q')
        # submitbutton = request.GET.get('submit')
        #
        # if query is not None:
        #     # lookups = Project(title__icontains=query)
        #
        #     projects = Project.objects.filter(title__startswith = query)
        #
        #     context = {
        #          'projects': projects
        #      }
        #
        #     return render(request, 'projects/search_result.html', context)
    # projects = None
    # if request.method == 'POST':
    #     projects = Project.objects.filter(title__startswith = request.POST)
    #
    #     return redirect('searchproj')
    #
    #
    # context = {
    #     'projects': projects
    # }

    # return render(request, 'projects/search_result.html')