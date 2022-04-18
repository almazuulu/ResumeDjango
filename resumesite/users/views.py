from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile, Skill
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import Profileform, ProfileEditForm, SkillForm
from .utils import searchProfiles, paginateProfiles

def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']

       try:
           user = User.objects.get(username = username)
       except:
           messages.error(request,'Данного пользователя не существует!')

       user = authenticate(request, username = username, password=password)

       if user is not None:
           login(request, user)
           return redirect(request.GET['next'] if 'next' in request.GET else 'account')
       else:
           messages.error(request,'Имя пользователя или пароль не совпадают!')

    context = {
        'page': page,
    }

    return render(request, 'users/login_register.html', context)


def logoutProfile(request):
    logout(request)
    messages.info(request, 'Пользователь успешно вышел!')
    return render(request, 'users/login_register.html' )

def registerUser(request):
    page = 'register'
    form = Profileform()
    context = {
      'page':page,
      'form':form
    }

    if request.method == 'POST':
        form = Profileform(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'Пользователь успешно зарегистрирован!')

            login(request, user)
            return redirect('editaccount')
        else:
            messages.error(request, 'Произошла ошибка во время регистрации пользователя!')
    return render(request, 'users/login_register.html', context=context)


def profiles(requests):
    profiles, search_query = searchProfiles(requests)

    results = 6

    custom_range, profiles = paginateProfiles(requests, profiles, results)

    context = {
        'profiles': profiles,
        'search_query':search_query,
        'custom_range': custom_range
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

@login_required(login_url='login')
def accountUser(requests):
    # user = Profile.objects.get(id=pk)
    profile = requests.user.profile

    skills = profile.skill_set.all()

    context = {
        'profile': profile,
        'skills': skills
    }
    return render(requests, 'users/account.html', context=context)

@login_required(login_url='login')
def editAccount(request):
    # user = Profile.objects.get(id=pk)
    profile = request.user.profile
    form = ProfileEditForm(instance=profile)

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('account')

    context = {'form': form}
    return render(request, 'users/profile_form.html', context)

@login_required(login_url='login')
def addSkills(request):
    profile = request.user.profile
    form = SkillForm()

    if request.method == 'POST':
        form = SkillForm(request.POST)

        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, 'Навык был успешно добавлен!')
            return redirect('account')

    context = {
        'form': form
    }

    return render(request, 'users/add_skills.html', context)

@login_required(login_url='login')
def updateSkills(request, pk):
    profile = request.user.profile

    skill = profile.skill_set.get(id = pk)
    form = SkillForm(instance=skill)

    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Навык был успешно обновлен!')
            return redirect('account')

    context = {
        'skill':skill,
        'form': form
    }

    return render(request, 'users/add_skills.html', context)

@login_required(login_url='login')
def deleteSkills(request,pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id = pk)

    if request.method == 'POST':

        #Skill.objects.filter(id=pk).delete()
        skill.delete()
        messages.error(request, 'Навык был удален!')
        return redirect('account')

    context = {
        'object': skill
    }

    return render(request, 'delete_form.html', context)
