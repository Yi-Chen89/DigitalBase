from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from calc.models import SteelGrade, SteelSection
from .serializers import SteelTypeSerializer, AllSteelGradesSerializer, SteelGradeSerializer, SteelSectionTypeSerializer, AllSteelSectionsSerializer, SteelSectionSerializer

from utils.steel_calcs import tension_yield, compression_FB_nonslender, flexure_yielding, shear_web_no_tensionfield



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
    length = inputData['steelSection']['length']

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
        result['tension'] = tension_yield(F_y=F_y, A_g=A_g)
    
    if compressionCheck:
        E = SteelGrade.objects.filter(id=steelGradeId).values_list('E', flat=True)[0]
        r = float(SteelSection.objects.filter(id=steelSectionId).values_list('r_y', flat=True)[0])
        L_c = length * 12
        result['compression'] = compression_FB_nonslender(E=E, F_y=F_y, A_g=A_g, r=r, L_c=L_c)

    if flexureCheck:
        Z_x = float(SteelSection.objects.filter(id=steelSectionId).values_list('Z_x', flat=True)[0])
        result['flexure'] = flexure_yielding(F_y=F_y, Z_x=Z_x) / 12
    
    if shearCheck:
        d = float(SteelSection.objects.filter(id=steelSectionId).values_list('d', flat=True)[0])
        t_w = float(SteelSection.objects.filter(id=steelSectionId).values_list('t_w', flat=True)[0])
        result['shear'] = shear_web_no_tensionfield(F_y=F_y, d=d, t_w=t_w)

    if torsionCheck:
        phi_T = 0.9
        result['torsion'] = 1


    return Response(result)