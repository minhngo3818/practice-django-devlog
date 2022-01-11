from django.shortcuts import render

projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by community'
    },
    {
        'id': '4',
        'title': 'Video Chat',
        'description': 'A video chat application'
    },
    {
        'id': '5',
        'title': '2D Game',
        'description': 'A video pixel game in 2D'
    }
]


# Create your views here.
def projects(request):
    context = {'projects': projectsList}
    return render(request, 'projects.html', context)


def project(request, pk):
    projectObject = None
    for i in projectsList:
        if i['id'] == str(pk):
            projectObject = i
    return render(request, 'single_project.html', {'project': projectObject})
