from django import forms
  
class add_data_Form(forms.Form):
    year = forms.IntegerField()
    data_file = forms.FileField()