from django.shortcuts import render
from django.http import HttpResponse


def projects(request):
    return render(request, 'projects/project.html')

def project(request, cookie):
    return render(request, 'projects/single-project.html')