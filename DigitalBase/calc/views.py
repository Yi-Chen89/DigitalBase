from django.shortcuts import render


def index(request):
    return render(request, 'calc/index.html')

def test(request):
    id, F_y, A = request.POST['id'], request.POST['yield'], request.POST['area']

    context = {'id': id,
               'F_y': F_y,
               'A': A}
    return render(request, 'calc/index.html', context)