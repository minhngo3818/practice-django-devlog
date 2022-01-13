from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm


# Create your views here.
def projects(request):
    proj = Project.objects.all()
    context = {'projects': proj}
    return render(request, 'projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    reviews = projectObj.reviews.all()
    context = {'project': projectObj, 'tags': tags, 'reviews': reviews}
    return render(request, 'single-project.html', context)


def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':            # signal to send data to backend
        form = ProjectForm(request.POST)    # find any data and past to form
        if form.is_valid():                 # check data is correct
            form.save()
            return redirect('projects')     # redirect to homepage

    context = {'form': form}
    return render(request, 'project-form.html', context)


def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)    # pass the editing object to a form

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)  # pass again the editing object to a form
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'project-form.html', context)


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    return render(request, 'delete.html', {'object': project})

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