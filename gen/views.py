from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'gen/home.html',)

def password(request):

    character = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        character.extend(list('!@#$%^&*()_+=-'))

    if request.GET.get('numbers'):
        character.extend(list('123456789'))


    lenght = int(request.GET.get('lenght',12))


    thepassword = ''
    for x in range(lenght):
        thepassword += random.choice(character)


    return render(request, 'gen/password.html', {'password': thepassword})

def about(request):
    return render(request, 'gen/about.html',)