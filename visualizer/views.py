from django.shortcuts import render
from .scripts.import_data import Excel_import
from django import forms
from visualizer import models as model
from .forms import add_data_Form
from rest_framework import viewsets, permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework.decorators import api_view
from django.http import Http404
from django.db.models import Sum

def handle_uploaded_file(f, year):
    context = {}
    Excel_import_processor = Excel_import(f, year)
    return Excel_import_processor.process_import(model)  

def dashboard(request, *args, **kwargs):
    return render(request, "dashboard.html", {})

def import_data(request, *args, **kwargs):
    context = {}
    if request.POST:
        form = add_data_Form(request.POST, request.FILES)
        if form.is_valid():
            result = handle_uploaded_file(request.FILES["data_file"],request.POST['year'])
            if result:
                context['message'] = 'data imported' 
            else:
                context['message'] = 'incorrect file structure' 
    else:
        form = add_data_Form()
    context['form'] = form
    return render(request, "add_data.html", context)

def delete_data(request, *args, **kwargs):
    context = {}
    try:
        model.Plant_information.objects.all().delete()
        model.Energy.objects.all().delete()
        model.Plant.objects.all().delete()
        context['result'] = True

    except Exception as E:
        context['error'] = E
        context['result'] = False
    return render(request, "delete_data.html", context)

class Plant(viewsets.ModelViewSet):
    """
    API endpoint to retrieve all Plant
    """
    queryset = model.Plant.objects.all().order_by('id')
    serializer_class = Plant_Serializer

class Plant_information_all(viewsets.ModelViewSet):
    """
    API endpoint to retrieve all Plant informations
    """
    queryset = model.Plant_information.objects.all().order_by('id')
    serializer_class = Plant_information_Serializer

class Energy_all(viewsets.ModelViewSet):
    """
    API endpoint to retrieve all Energy
    """
    queryset = model.Energy.objects.all().order_by('id')
    serializer_class = Energy_Serializer

class Plant_information(generics.ListAPIView):
    """
    Retrieve Plans informations for the giving year
    """
    serializer_class = Plant_information_Serializer
    def get_queryset(self):
        year = self.kwargs['year']
        return model.Plant_information.objects.filter(year=year).order_by('id')

class Energy(generics.ListAPIView):
    """
    Retrieve Energies for the giving year
    """
    serializer_class = Energy_Serializer
    def get_queryset(self):
        year = self.kwargs['year']
        return model.Energy.objects.filter(year=year).order_by('id')

class Energy_summed(generics.ListAPIView):
    """
    Retrieve Energies for the giving year
    """
    serializer_class = Energy_Serializer_sum
    def get_queryset(self):
        year = self.kwargs['year']
        result = model.Energy.objects.filter(year=year).values('plant_information').annotate(Sum('generator_anual_net')).order_by('id')
        print(result)
        return result
