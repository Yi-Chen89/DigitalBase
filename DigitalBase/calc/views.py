from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from calc.models import SteelGrade, SteelSection
from .serializers import SteelTypeSerializer, AllSteelGradesSerializer, SteelGradeSerializer, SteelSectionTypeSerializer, AllSteelSectionsSerializer, SteelSectionSerializer

from utils.steel_calcs import tension_yield, compression_FB_nonslender, flexure_yielding, shear_web_no_tensionfield
from utils.arup_compute import arup_compute_tension_yielding, arup_compute_flexure_strength


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

    response = {
        'material': {
            'F_y': F_y,
            'F_u': F_u,
            'E': None,
        },
        'property': {
            'A_g': A_g,
            'd': None,
            'b_f': None,
            't_w': None,
            't_f': None,
            'k_des': None,
            'I_x': None,
            'Z_x': None,
            'S_x': None,
            'r_x': None,
            'I_y': None,
            'Z_y': None,
            'S_y': None,
            'r_y': None,
            'J': None,
            'C_w': None,
            'h_o': None,
        },
        'result': {
            'tension': None,
            'tension_ac': None,
            'compression': None,
            'flexure': None,
            'flexure_ac': None,
            'shear': None,
            'torsion': None,
        },
    }


    if tensionCheck:
        response['result']['tension'] = tension_yield(F_y=F_y, A_g=A_g)

        P_n, html_style, html = arup_compute_tension_yielding(F_y=F_y, A_g=A_g)
        response['result']['tension_ac'] = html

    
    if compressionCheck:
        E = SteelGrade.objects.filter(id=steelGradeId).values_list('E', flat=True)[0]
        r = float(SteelSection.objects.filter(id=steelSectionId).values_list('r_y', flat=True)[0])
        L_c = length * 12
        response['result']['compression'] = compression_FB_nonslender(E=E, F_y=F_y, A_g=A_g, r=r, L_c=L_c)


    if flexureCheck:
        Z_x = float(SteelSection.objects.filter(id=steelSectionId).values_list('Z_x', flat=True)[0])
        response['result']['flexure'] = flexure_yielding(F_y=F_y, Z_x=Z_x) / 12

        r_y = float(SteelSection.objects.filter(id=steelSectionId).values_list('r_y', flat=True)[0])
        S_x = float(SteelSection.objects.filter(id=steelSectionId).values_list('S_x', flat=True)[0])
        J = float(SteelSection.objects.filter(id=steelSectionId).values_list('J', flat=True)[0])
        h_o = float(SteelSection.objects.filter(id=steelSectionId).values_list('h_o', flat=True)[0])
        I_y = float(SteelSection.objects.filter(id=steelSectionId).values_list('I_y', flat=True)[0])
        I_x = float(SteelSection.objects.filter(id=steelSectionId).values_list('I_x', flat=True)[0])
        b_f = float(SteelSection.objects.filter(id=steelSectionId).values_list('b_f', flat=True)[0])
        t_f = float(SteelSection.objects.filter(id=steelSectionId).values_list('t_f', flat=True)[0])
        k_des = float(SteelSection.objects.filter(id=steelSectionId).values_list('k_des', flat=True)[0])
        d = float(SteelSection.objects.filter(id=steelSectionId).values_list('d', flat=True)[0])
        t_w = float(SteelSection.objects.filter(id=steelSectionId).values_list('t_w', flat=True)[0])

        M_c, html_style, html = arup_compute_flexure_strength(F_y=F_y, Z_x=Z_x, r_y=r_y, L_b=L_c, S_x=S_x, J=J, h_o=h_o, I_y=I_y, I_x=I_x, b_f=b_f, t_f=t_f, k_des=k_des, d=d, t_w=t_w)
        response['result']['flexure_ac'] = html

    
    if shearCheck:
        d = float(SteelSection.objects.filter(id=steelSectionId).values_list('d', flat=True)[0])
        t_w = float(SteelSection.objects.filter(id=steelSectionId).values_list('t_w', flat=True)[0])
        response['result']['shear'] = shear_web_no_tensionfield(F_y=F_y, d=d, t_w=t_w)


    if torsionCheck:
        phi_T = 0.9
        response['result']['torsion'] = 1


    return Response(response)