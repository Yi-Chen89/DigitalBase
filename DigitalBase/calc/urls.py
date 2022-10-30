from django.urls import path

from . import views

app_name = 'calc'
urlpatterns = [
    path('steelgrades/', views.getAllSteelGrades),
    path('steelgrade/<int:id>', views.getSteelGrade),
    path('steelsections/', views.getAllSteelSections),
    path('steelsection/<int:id>', views.getSteelSection),

    path('steelcalc', views.steelCalc)
]