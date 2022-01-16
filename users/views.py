from django.shortcuts import render
from .models import Profile


# Create your views here.
def profiles(request):
    profiles_obj = Profile.objects.all()
    context = {'profiles': profiles_obj}
    return render(request, 'users/profiles.html', context)
