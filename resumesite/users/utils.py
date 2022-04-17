from .models import Profile, Skill
from django.db.models import Q


def searchProfiles(requests):
    search_query = ''

    if requests.GET.get('search_query'):
        search_query = requests.GET.get('search_query')

    # print(f'Result: {search_query}')

    skills = Skill.objects.filter(name__icontains=search_query)

    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(short_intro__icontains=search_query) |
        Q(skill__in=skills)
    )

    return profiles, search_query