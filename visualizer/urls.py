from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('plant_list', views.PlantAPIView, basename='plant_list')


urlpatterns = [
    url('', include(router.urls)),
]