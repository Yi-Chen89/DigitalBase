from django.shortcuts import render
from django.http import JsonResponse

from project.models import Project, Scope


def index(request):
    project_list = Project.objects.all()

    context = {'project_list': project_list}

    return render(request, 'project\index.html', context)


def get_project_info(request, id):
    if request.method == 'GET':
        project_list = Project.objects.all()
        project_info = Project.objects.filter(id=id).first()
        project_scope = Scope.objects.filter(project_id=id)
        
        context = {'project_list': project_list,
                   'project_info': project_info,
                   'project_scope': project_scope}

        return render(request, 'project\index.html', context)

        # for AJAX
        # return JsonResponse(info, safe=False)