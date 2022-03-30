from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def projects(request):
    #return HttpResponse("Hello from projects")
    return render(request, 'projects.html')

def project(request, pk):
    #return HttpResponse("Hello there!" + " " + str(pk))
    return render(request, 'single-project.html')


