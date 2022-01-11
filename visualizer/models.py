from django.db import models


class Plant(models.Model):
    name = models.CharField(max_length=60)
    facility_code = models.IntegerField(unique=True)
    state = models.CharField(max_length=5)
    latitude = models.DecimalField(default=None, blank=True, null=True, max_digits=10, decimal_places=6)
    longitude  = models.DecimalField(default=None, blank=True, null=True, max_digits=10, decimal_places=6)


class Plant_information(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    primary_fuel = models.CharField(default=None, blank=True, null=True, max_length=5)
    num_generator = models.IntegerField(default=None, blank=True, null=True)
    nameplate_capacity = models.DecimalField(default=None, blank=True, null=True, max_digits=15, decimal_places=3)
    num_boilers = models.IntegerField(default=None, blank=True, null=True)
    year = models.IntegerField()

class Energy(models.Model):
    plant_information = models.ForeignKey(Plant_information, on_delete=models.CASCADE)
    generator_id = models.CharField(max_length=10)
    generator_anual_net = models.DecimalField(default=0, blank=True, null=True, max_digits=15, decimal_places=3)
    year = models.IntegerField()

