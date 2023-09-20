from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Project,Task
from django.shortcuts import get_object_or_404, render,redirect
from .forms import CreateNewTask, CreateNewProject

def index(request):
    title='Django Course!!'
    return render(request,'index.html',{
        'title':title
    })

def hello(request,username):
    return HttpResponse("<div><h1>Hello World</h1><p>Mi nombre es %s </p></div>" %username)
def about(request):
    username='sebas'
    return render(request,'about.html',{
        'username':username
    })
# Create your views here.
def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request,'projects/projects.html',{
        'projects':projects
    })

def tasks(request):
    tasks=Task.objects.all()
    #task=get_object_or_404(Task,id=id)
    return render(request,'tasks/tasks.html',{
        'tasks':tasks
    })

def create_task(request):

    if request.method=='GET':
        return render(request,'tasks/create_tasks.html',{
            'form':CreateNewTask()
        })
    else:

        Task.objects.create(title=request.POST['title'],description=request.POST['description'],
                            project_id=request.POST['project'])
        return redirect('tasks')

def create_project(request):
    if request.method=='GET':
        return render(request,'projects/create_projects.html',{
            'form':CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST["name"])
        return redirect('projects')

def project_detail(request,id):

    project=get_object_or_404(Project,id=id)
    tasks=Task.objects.filter(project_id=id)

    return render(request,'projects/details.html',{
        'project':project,
        'tasks':tasks
    })

def delete_project(request):
    if request.method=='GET':
        return render(request,'projects/projects.html')
    else:
        
        Project.objects.delete(id=request.POST["id"])
        print(id)
        return redirect('projects')


