from django.urls import path

from . import views

app_name = 'calc'
urlpatterns = [
    path('steelsection/', views.getAllSteelSection),
    path('steelsection/<int:id>', views.getSteelSection),
]