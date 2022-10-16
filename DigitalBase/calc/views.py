from rest_framework.response import Response
from rest_framework.decorators import api_view

from calc.models import SteelSection
from .serializers import SteelSectionSerializer

from django.shortcuts import render


def index(request):
    return render(request, 'calc/index.html')

def test(request):
    id, F_y, A = request.POST['id'], request.POST['yield'], request.POST['area']

    context = {'id': id,
               'F_y': F_y,
               'A': A}
    return render(request, 'calc/index.html', context)


@api_view(['GET'])
def getAllSteelSection(request):
    steel_section = SteelSection.objects.all()
    serializer = SteelSectionSerializer(steel_section, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSteelSection(request, id):
    steel_section = SteelSection.objects.get(pk=id)
    serializer = SteelSectionSerializer(steel_section, many=False)
    return Response(serializer.data)