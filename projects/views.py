from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Project
from .form import ProjectForm

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {'projects':projects})

def project(request, pk):
    
    project = Project.objects.get(id=pk)
    print(project)
    # for project in data:
    #     if project['id'] == str(pk):
    #         content = project
    context = {'project':project}
    return render(request, 'projects/project.html', context)

def create_project(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'project':form}
    return render(request, 'projects/form-project.html', context)
# INTERT INTO project.public (id, title, description../) VALUES ()

def delete_project(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect('projects')
    context = {'object':project}
    return render(request, 'projects/delete-project.html', context)


def update_project(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'project':form}
    return render(request, 'projects/form-project.html', context)
