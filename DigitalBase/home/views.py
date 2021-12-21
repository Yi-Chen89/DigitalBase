from django.http import HttpResponse

from django.shortcuts import render

# All apps
APPS = ['project']

FUTURE_APPS = ['project',
               'task',
               'calc',
               'tool',
               'data']


def index(request):
    context = {'blocks': FUTURE_APPS,
               'apps': APPS,
               'add_base': True}
    return render(request, 'home\index.html', context)