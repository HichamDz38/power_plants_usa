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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from visualizer import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

router = DefaultRouter()
router.register(r'power_plants', views.Plant)
router.register(r'plant_informations', views.Plant_information_all)
router.register(r'energies', views.Energy_all)

urlpatterns = (
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.png'))),
    path('add_data/', views.import_data, name='import_data'),
    path('del_data/', views.delete_data, name='delete_data'),
    path('power_plants/<int:year>/', views.Plant_information.as_view()),
    path('energies/<int:year>/', views.Energy.as_view()),
    path('energies/<int:year>/<int:limit>/', views.Energy_limited.as_view()),
    path('energies/<int:year>/<str:state>/', views.Energy_by_state.as_view()),
    path('energies/<int:year>/<str:state>/<int:limit>/', views.Energy_by_state_limited.as_view()),
    path('energies_summary/<int:year>/', views.Energy_summary.as_view()),
    path('years/', views.Data_years.as_view()),
    path('api/', include(router.urls)),
)
