from abc import ABC, abstractmethod
import openpyxl
from openpyxl import load_workbook
import logging

logger = logging.getLogger(__name__)

class Import_data(ABC):

    @abstractmethod
    def process_import(self):
        pass


class Excel_import(Import_data):

    def __init__(self, filename, year):
        self.file = filename
        self.year = year
        self.year_pre = str(year)[2:]

    def process_import(self, model):
        try:
            book = openpyxl.load_workbook(self.file)
            plants_sheet = book['PLNT'+self.year_pre]
            generators_sheet = book['GEN'+self.year_pre]
            plant_model = model.Plant
            plant_info_model = model.Plant_information
            enery_model = model.Energy
            self.save_plants(plants_sheet, plant_model, plant_info_model)
            self.save_energy(generators_sheet, plant_model, plant_info_model, enery_model)
            logger.warning('import data done')
        except KeyError as E:
            logger.exception(E)
            return False      

    def save_plants(self, plants_sheet, plant_model, plant_info_model):
        for row in plants_sheet.iter_rows(min_row=3):
            name = row[2].value
            facility_code = row[3].value
            state = row[1].value
            latitude = row[17].value
            longitude = row[18].value
            primary_fuel = row[21].value
            num_generator = row[20].value
            nameplate_capacity = row[25].value
            num_boilers = row[19].value
            year = self.year
            try:
                plant = plant_model.objects.create(name=name, facility_code=facility_code, state=state,
                                                   latitude=latitude, longitude=longitude)
                plant_info_model.objects.create(plant=plant, primary_fuel=primary_fuel, num_generator=num_generator,
                                                nameplate_capacity=nameplate_capacity, num_boilers=num_boilers,
                                                year=year)
            except Exception as E:
                logger.exception(E)


    def save_energy(self, generators_sheet, plant_model, plant_info_model, enery_model):
        for row in generators_sheet.iter_rows(min_row=3):            
            facility_code = row[3].value
            generator_id = row[4].value
            generator_anual_net = row[11].value
            year = self.year
            try:
                plant = plant_model.objects.get(facility_code=facility_code)
                plant_information = plant_info_model.objects.get(plant=plant)
                enery_model.objects.create(plant_information=plant_information, generator_id=generator_id,
                                           generator_anual_net=generator_anual_net, year=year)
            except Exception as E:
                logger.exception(E)
