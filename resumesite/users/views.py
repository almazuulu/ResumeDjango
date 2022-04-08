from django.shortcuts import render

# Create your views here.
def profiles(requests):
    message = 'Hello there!'

    context = {
        'message': message
    }
    return render(requests,'users/profiles.html', context=context)