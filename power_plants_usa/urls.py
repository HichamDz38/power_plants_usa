"""power_plants_usa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from visualizer import views

router = DefaultRouter()
router.register(r'plant_list', views.Plant)
router.register(r'plant_information', views.Plant_information_all)
router.register(r'energy', views.Energy_all)

urlpatterns = (
    path('add_data/', views.import_data, name='import_data'),
    path('del_data/', views.delete_data, name='delete_data'),
    re_path(r'^plant_information/(?P<year>[0-9]+)/$', views.Plant_information.as_view()),
    path('api/', include(router.urls)),
)
