from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional Ecommerce Platform'
    },

    {
        'id': '2',
        'title': 'Project Protfolio',
        'description': 'My Prject protfolio'
    },

    {
        'id': '3',
        'title': 'Some another portfolio',
        'description': 'Last project description'
    },



]

def projects(request):
    someName  = 'Askarbek'
    context = {
        'name': someName,
        'projectslist': projectsList
    }
    return render(request, 'projects/projects.html', context= context)

def project(request, pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i

    context = {
        'project': projectObj
    }

    return render(request, 'projects/single-project.html', context= context)


