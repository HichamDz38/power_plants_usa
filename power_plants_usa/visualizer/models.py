from django.db import models

# Create your models here.


class Plant(models.Model):
    name 
    facility_code
    state_abrv
    latitude
    longitude

class Energy(models.Model):
    Plant_id
    year
    generator_id

