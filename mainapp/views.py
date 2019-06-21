from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect
from django.urls import reverse

from .models import Project
# Create your views here.


def home(request):
    return render(request,'mainapp/home.html')


def projects(request):
    projects_list = Project.objects.order_by('-pub_date').all()
    context = {
        'projects_list':projects_list
    }
    return render(request,'mainapp/projects.html',context)

def project_detail(request,project_id):
    context = {
        'project_id':project_id
    }
    return render(request,'mainapp/project_detail.html',context)