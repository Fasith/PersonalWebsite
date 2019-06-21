from django.urls import path
from . import views

app_name = "mainapp"

urlpatterns = [
    path('',views.home,name='home'),
    path('projects/',views.projects,name='projects'),
    path('project/<int:project_id>/',views.project_detail,name='project_detail')
]