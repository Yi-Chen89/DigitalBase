from django.http import HttpResponse

from django.shortcuts import render

# All apps
APPS = ['project',
        'task',
        'calc',
        'tool',
        'data']


def index(request):
    context = {'blocks': APPS,
               'add_base': True}
    return render(request, 'home\index.html', context)