from rest_framework import serializers

from calc.models import SteelType, SteelGrade, SteelSectionType, SteelSection


class SteelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SteelType
        fields = '__all__' 


class SteelGradeSerializer(serializers.ModelSerializer):
    type = SteelTypeSerializer(many=False)

    class Meta:
        model = SteelGrade
        fields = '__all__' 


class SteelSectionTypeSerializer(serializers.ModelSerializer):
    preferred_steel = SteelGradeSerializer(many=False)

    class Meta:
        model = SteelSectionType
        fields = '__all__' 


class AllSteelSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SteelSection
        fields = ['id',
                  'name']


class SteelSectionSerializer(serializers.ModelSerializer):
    type = SteelSectionTypeSerializer(many=False)

    class Meta:
        model = SteelSection
        fields = '__all__'