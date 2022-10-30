from rest_framework.response import Response
from rest_framework.decorators import api_view

from calc.models import SteelGrade, SteelSection
from .serializers import SteelTypeSerializer, AllSteelGradesSerializer, SteelGradeSerializer, SteelSectionTypeSerializer, AllSteelSectionsSerializer, SteelSectionSerializer



@api_view(['GET'])
def getAllSteelGrades(request):
    all_steel_grades = SteelGrade.objects.all()
    serializer = AllSteelGradesSerializer(all_steel_grades, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getSteelGrade(request, id):
    steel_grade = SteelGrade.objects.get(pk=id)
    serializer = SteelGradeSerializer(steel_grade, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getAllSteelSections(request):
    all_steel_sections = SteelSection.objects.all()
    serializer = AllSteelSectionsSerializer(all_steel_sections, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getSteelSection(request, id):
    steel_section = SteelSection.objects.get(pk=id)
    serializer = SteelSectionSerializer(steel_section, many=False)
    return Response(serializer.data)