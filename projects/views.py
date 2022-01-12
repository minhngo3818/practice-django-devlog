from django.shortcuts import render
from .models import Project


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
    return render(request, 'single_project.html', context)

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