from django.shortcuts import render
from django import forms
from django.http import Http404
from django.db.models import Sum
from visualizer import models as model
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from .serializers import *
from .forms import add_data_Form
from .scripts.import_data import Excel_import



def handle_uploaded_file(f, year):
    file_name = 'uploaded_file_{}'.format(f)
    with open(file_name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    context = {}
    Excel_import_processor = Excel_import(file_name, year)
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
        return model.Energy.objects.filter(year=year).exclude(plant_information__plant=None).exclude(plant_information__plant__longitude=None).exclude(plant_information__plant__latitude=None).order_by('id')

class Energy_limited(generics.ListAPIView):
    """
    Retrieve Energies for the giving year
    """
    serializer_class = Energy_Serializer
    def get_queryset(self):
        year = self.kwargs['year']
        limit = self.kwargs['limit']
        return model.Energy.objects.filter(year=year).exclude(plant_information__plant=None).exclude(plant_information__plant__longitude=None).exclude(plant_information__plant__latitude=None).order_by('-generator_anual_net')[:limit]

class Energy_by_state(generics.ListAPIView):
    """
    Retrieve Energies for the giving year/state
    """
    serializer_class = Energy_Serializer_by_state
    def get_queryset(self):
        year = self.kwargs['year']
        state = self.kwargs['state']
        return model.Energy.objects.filter(year=year).filter(plant_information__plant__state=state).exclude(plant_information__plant__longitude=None).exclude(plant_information__plant__latitude=None).order_by('id')

class Energy_by_state_limited(generics.ListAPIView):
    """
    Retrieve Energies for the giving year/state
    """
    serializer_class = Energy_Serializer_by_state
    def get_queryset(self):
        year = self.kwargs['year']
        state = self.kwargs['state']
        limit = self.kwargs['limit']
        return model.Energy.objects.filter(year=year).filter(plant_information__plant__state=state).exclude(plant_information__plant__longitude=None).exclude(plant_information__plant__latitude=None).order_by('-generator_anual_net')[:limit]
