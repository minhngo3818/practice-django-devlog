from .models import Profile, Skill
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def paginateProfiles(request, profile_objects, results):
    page = request.GET.get('page')
    paginator = Paginator(profile_objects, results)

    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)

    # Set up limit to show number of pages when there are too much
    leftIndex = (int(page) - 1)
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 2)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, profiles


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
