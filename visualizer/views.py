from django.shortcuts import render
from .scripts.import_data import Excel_import
from django import forms
from visualizer import models as model
from .forms import add_data_Form
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import Plant_Serializer,Plant_information_Serializer,Energy_Serializer


def handle_uploaded_file(f, year):
    Excel_import_processor = Excel_import(f, year)
    return Excel_import_processor.process_import(model)


def dashboard(request, *args, **kwargs):
    return render(request, "dashboard.html", {})


def import_data(request, *args, **kwargs):
    context = {}
    if request.POST:
        form = add_data_Form(request.POST, request.FILES)
        if form.is_valid():
            status = handle_uploaded_file(request.FILES["data_file"],request.POST['year'])
            context['status'] = status
    else:
        form = add_data_Form()
    context['form'] = form
    return render(request, "add_data.html", context)

def delete_data(request, *args, **kwargs):
    context = {}
    try:
        model.Plant_information.objects().all().delete()
        model.Energy.objects().all().delete()
        model.Plant.objects().all().delete()
        context['result'] = True

    except Exception as E:
        context['error'] = Energy
        context['result'] = False
    return render(request, "delate_data.html", context)

class PlantAPIView(viewsets.ModelViewSet):
    """
    API endpoint for Plant
    """
    queryset = model.Plant.objects.all().order_by('id')
    serializer_class = Plant_Serializer

class Plant_informationAPIView(viewsets.ModelViewSet):
    """
    API endpoint for Plant
    """
    queryset = model.Plant_information.objects.all().order_by('id')
    serializer_class = Plant_information_Serializer

class EnergyAPIView(viewsets.ModelViewSet):
    """
    API endpoint for Plant
    """
    queryset = model.Energy.objects.prefetch_related('plant').order_by('id')
    serializer_class = Energy_Serializer
