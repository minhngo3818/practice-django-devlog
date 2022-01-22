from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Project, Tag
from .forms import ProjectForm
from .utils import searchProjects


# Create your views here.
def projects(request):

    projects, search_query = searchProjects(request)

    context = {'projects': projects, 'search_query': search_query}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    reviews = projectObj.reviews.all()
    context = {'project': projectObj, 'tags': tags, 'reviews': reviews}
    return render(request, 'projects/single-project.html', context)


@login_required(login_url='login')     # decorator to require user login to view/ restrict to member user
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':            # signal to send data to backend
        form = ProjectForm(request.POST, request.FILES)    # find any data and past to form
        if form.is_valid():                 # check data is correct
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('account')     # redirect to homepage

    context = {'form': form}
    return render(request, 'projects/project-form.html', context)


@login_required(login_url='login')
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)    # pass the editing object to a form

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)  # pass again the editing object to a form
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {'form': form}
    return render(request, 'project-form.html', context)


@login_required(login_url='login')
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    context = {'object': project}
    return render(request, 'delete.html', context)

# Put this into template if using right access obj in templates
# <!-- To access right on template follow belows
# {% for tag in project.tags.all() %}
#                         ^
#                   access related_obj
# {% endfor %} -->



# projectsList = [
#     {
#         'id': '1',
#         'title': 'Ecommerce Website',
#         'description': 'Fully functional ecommerce website'
#     },
#     {
#         'id': '2',
#         'title': 'Portfolio Website',
#         'description': 'A personal website to write articles and display'
#     },
#     {
#         'id': '3',
#         'title': 'Social Network',
#         'description': 'An open source project built by community'
#     },
#     {
#         'id': '4',
#         'title': 'Video Chat',
#         'description': 'A video chat application'
#     },
#     {
#         'id': '5',
#         'title': '2D Game',
#         'description': 'A video pixel game in 2D'
#     }
# ]