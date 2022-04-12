from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import Profileform

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
           return redirect('profiles')
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
            return redirect('profiles')
        else:
            messages.error(request, 'Произошла ошибка во время регистрации пользователя!')
    return render(request, 'users/login_register.html', context=context)

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

#@login_required(Login_url='login')
#def editAccount(requests, pk):
    #user = Profile.objects.get(id=pk)

    #return render(requests, 'users/account.html', context=context)