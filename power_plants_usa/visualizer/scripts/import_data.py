from abc import ABC, abstractmethod
import openpyxl

class Import_data(ABC):

    @abstractmethod
    def import(self):
        pass


class Excel_import(Import_data):

    def __init___(self, filename, year):
        self.file = filename
        self.year = year
        self.year_pre = str(year)[:2]

    def import(self, model):
        book = openpyxl.open_workbook(self.file)
        plants_sheet = book['PLNT'+self.year_pre]
        generators_sheet = book['GEN'+self.year_pre]
        plant_model = model.Plant
        plant_info_model = model.Plant_information
        enery_model = model.Energy
        save_plants(plants_model, plants_info_model, plants_sheet)
        save_energy(generators_sheet, plants_model, enery_model)
        
    def save_plants(self, plants_sheet, plants_model, plants_info_model):
        for i, row in plants_sheet.iter_rows():
            if i==0 :
                continue
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
            plant = plants_model.objects.create(name=name, facility_code=facility_code, state=state,
                                                latitude=latitude, longitude=longitude)
            plants_info_model.objects.create(plant=plant, primary_fuel=primary_fuel, num_generator=num_generator,
                                             nameplate_capacity=nameplate_capacity, num_boilers=num_boilers,
                                             year=year)

    def save_energy(self, generators_sheet, plants_model, enery_model):
        for i, row in generators_sheet.iter_rows():
            if i==0 :
                continue            
            facility_code = row[3].value
            generator_id = row[4].value
            generator_anual_net = row[11].value
            plant = plant_model.objects.get(facility_code=facility_code)
            enery_model.objects.create(plant=plant, generator_id=generator_id,
                                       generator_anual_net=generator_anual_net)
