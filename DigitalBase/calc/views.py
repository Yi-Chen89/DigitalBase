from rest_framework.response import Response
from rest_framework.decorators import api_view

from calc.models import SteelSection
from .serializers import AllSteelSectionSerializer, SteelSectionSerializer


@api_view(['GET'])
def getAllSteelSection(request):
    all_steel_section = SteelSection.objects.all()
    serializer = AllSteelSectionSerializer(all_steel_section, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSteelSection(request, id):
    steel_section = SteelSection.objects.get(pk=id)
    serializer = SteelSectionSerializer(steel_section, many=False)
    return Response(serializer.data)