from django.contrib import admin

from calc.models import ASCE7Version, DesignMethod, LoadCombination, AISC360Version, SteelType, SteelGrade, SteelSectionType, SteelSection


admin.site.register(ASCE7Version)
admin.site.register(DesignMethod)
admin.site.register(LoadCombination)
admin.site.register(AISC360Version)

admin.site.register(SteelType)
admin.site.register(SteelGrade)
admin.site.register(SteelSectionType)
admin.site.register(SteelSection)