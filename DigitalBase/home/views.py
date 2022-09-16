from django.http import HttpResponse

from django.shortcuts import render

# All apps
APPS = ['project',
        'calc']

FUTURE_APPS = ['project',
               'task',
               'calc',
               'tool',
               'data']


def index(request):
    context = {'blocks': APPS,
               'apps': APPS,
               'add_base': True}
    return render(request, 'home\index.html', context)