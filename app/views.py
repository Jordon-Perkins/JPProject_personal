from django.shortcuts import render
from django.template import loader
from .models import Project
from django.http import HttpResponse


def index(request):
    project_list = Project.objects.all()
    output = ", ".join([q.title for q in project_list])
    template = loader.get_template("app/index.html")
    context = {
        "project_list": project_list,
    }
    return HttpResponse(template.render(context, request))