from rest_framework import serializers

from calc.models import SteelSectionType, SteelSection


class SteelSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SteelSection
        fields = '__all__'