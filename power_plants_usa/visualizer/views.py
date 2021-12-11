from django.shortcuts import render
from .scripts.import_data import Excel_import
from django import forms
from . import models as model
from .forms import add_data_Form


def handle_uploaded_file(f):
    Excel_import_processor = Excel_import(f, 2016)
    return Excel_import_processor.process_import(model)


def dashboard(request, *args, **kwargs):
    return render(request, "dashboard.html", {})


def import_data(request, *args, **kwargs):
    context = {}
    if request.POST:
        form = add_data_Form(request.POST, request.FILES)
        if form.is_valid():
            status = handle_uploaded_file(request.FILES["data_file"])
            context['status'] = status
    else:
        form = add_data_Form()
    context['form'] = form
    return render(request, "add_data.html", context)
