from django.shortcuts import render


# Create your views here.

def login(request):
    context = {
        "SIGN_IN": False
    }
    return render(request, 'auth/login.html', context)
