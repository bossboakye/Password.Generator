from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, 'generator/index.html')


def password(request):
    characters = list('')

    if request.GET.get('lower'):
        characters.extend(list('abcdefghijklmnopqrstuvwxyz'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_-+='))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length', 10))

    thepassword = ''

    if len(characters) > 0:
        for i in range(length):
            thepassword += random.choice(characters)
        return render(request, 'generator/password.html', {'password': thepassword})

    else:
        return render(request, 'generator/error.html')


def about(request):
    return render(request, 'generator/about.html')
