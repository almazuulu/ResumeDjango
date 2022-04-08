from django.shortcuts import render
from .models import Profile

# Create your views here.
def profiles(requests):
    profiles = Profile.objects.all()


    context = {
        'profiles': profiles
    }
    return render(requests,'users/profiles.html', context=context)

def profile(requests, pk):
    profile = Profile.objects.get(id = pk)

    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")

    context = {
        'profile': profile,
        'topSkills': topSkills,
        'otherSkills':otherSkills
    }

    return render(requests, 'users/profile.html', context=context)
