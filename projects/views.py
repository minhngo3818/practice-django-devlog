from django.shortcuts import render

projectList = [
    {
        'id': 1,
        'title': '',
        'description': ''
    },
    {
        'id': 2,
        'title': '',
        'description': ''
    },
    {
        'id': 3,
        'title': '',
        'description': ''
    },
    {
        'id': 4,
        'title': '',
        'description': ''
    },
    {
        'id': 4,
        'title': '',
        'description': ''
    }
]


# Create your views here.
def projects(request):
    return render(request, 'projects.html')


def single_project(request, pk):
    return render(request, 'single_project.html')
