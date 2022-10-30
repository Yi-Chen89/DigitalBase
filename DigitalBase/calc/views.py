from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

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



@api_view(['POST'])
def steelCalc(request):
    inputData = JSONParser().parse(request)
    
    tensionCheck = inputData['checks']['tensionCheck']
    compressionCheck = inputData['checks']['compressionCheck']
    flexureCheck = inputData['checks']['flexureCheck']
    shearCheck = inputData['checks']['shearCheck']
    torsionCheck = inputData['checks']['torsionCheck']

    steelSectionId = inputData['steelSection']['steelSectionId']
    steelGradeId = inputData['steelSection']['steelGradeId']

    F_y = SteelGrade.objects.filter(id=steelGradeId).values_list('F_y', flat=True)[0]
    F_u = SteelGrade.objects.filter(id=steelGradeId).values_list('F_u', flat=True)[0]

    A_g = float(SteelSection.objects.filter(id=steelSectionId).values_list('A', flat=True)[0])

    result = {
        'tension': None,
        'compression': None,
        'flexure': None,
        'shear': None,
        'torsion': None,
    }

    if tensionCheck:
        phi_t = 0.9
        P_n = F_y * A_g
        result['tension'] = phi_t * P_n
    
    if compressionCheck:
        phi_c = 0.9
        result['compression'] = 1

    if flexureCheck:
        phi_b = 0.9
        result['flexure'] = 2
    
    if shearCheck:
        phi_v = 0.9
        result['shear'] = 3

    if torsionCheck:
        phi_T = 0.9
        result['torsion'] = 4


    return Response(result)