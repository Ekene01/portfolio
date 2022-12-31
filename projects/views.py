from django.shortcuts import render
from django.shortcuts import render
from django.urls import reverse

from .models import Project
# Create your views here.
def index(request):
    return render(request, "projects/index.html", {
        "projects": Project.objects.all()
    })

def project_details(request, project_id):
    project = Project.objects.get(pk=project_id)
    return render(request, "projects/project_details.html", {
        "project": project,

    })