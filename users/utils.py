from .models import Profile, Skill
from django.db.models import Q


def searchProjects(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        print('SEARCH:', search_query)

    skills = Skill.objects.filter(name__icontains=search_query)

    profiles_obj = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(short_intro__icontains=search_query) |
        Q(skill__in=skills)
    )

    return profiles_obj, search_query
