from django.shortcuts import render
# from django.views.generic import CreateView
from django.http import HttpResponse, HttpResponseRedirect
from .models import Records, Projects
from .forms import CreateProjectForm


# Create your views here.
def index(request):
    print(request.GET)
    projects_object = Projects.objects.all()
    return render(request, 'index.html', {'projects': projects_object})


def create_project(request):
    form = CreateProjectForm()
    if request.method == 'POST':
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            project = Projects(title=request.POST['title'], description=request.POST['description'])
            project.save()
            return HttpResponseRedirect(redirect_to='/?project_created=1')
        replies = {k: v for k, v in request.POST.items()}
        return HttpResponse(f"Reply info: {replies}")
    else:
        return render(request, 'create_project.html', {"form": form})

def project(request):
    print(request.GET)