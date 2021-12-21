from django.urls import path

from . import views

app_name = 'project'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.get_project_info, name='get_project_info'),
]