from django.db import models


class Plant(models.Model):
    name = models.CharField(max_length=30)
    facility_code = models.IntegerField()
    state = models.CharField(max_length=3)
    latitude = models.DecimalField()
    longitude  = models.DecimalField()


class Plant_information(models.Model):
    plant_id = models.IntegerField()
    primary_fuel = models.CharField(max_length=5)
    num_generator = models.IntegerField()
    nameplate_capacity = models.DecimalField()
    num_boilers = models.IntegerField()
    year = models.IntegerField()

class Energy(models.Model):
    Plant_id = models.IntegerField()
    generator_id =models.IntegerField()
    unit_id = models.IntegerField()
    year = models.IntegerField()

