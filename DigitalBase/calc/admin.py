from django.contrib import admin

from calc.models import SteelSectionType, SteelSection, SteelType, SteelGrade

admin.site.register(SteelSectionType)
admin.site.register(SteelSection)
admin.site.register(SteelType)
admin.site.register(SteelGrade)