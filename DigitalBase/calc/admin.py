from django.contrib import admin

from calc.models import SteelType, SteelGrade, SteelSectionType, SteelSection


admin.site.register(SteelType)
admin.site.register(SteelGrade)
admin.site.register(SteelSectionType)
admin.site.register(SteelSection)