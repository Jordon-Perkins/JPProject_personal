from django.shortcuts import render

# Create your views here.
from .models import Project

from django.http import HttpResponse


def index(request):
    project_list = Project.objects.all()
    output = ", ".join([q.title for q in project_list])
    return HttpResponse(output)
