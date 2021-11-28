from django.http import HttpResponse

from django.shortcuts import render

# All apps
APPS = ['project',
        'task',
        'calc',
        'tool',
        'data']

# APPS = ['project',]

def index(request):
    context = {'apps': APPS}
    return render(request, 'home\index.html', context)