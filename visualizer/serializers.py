from rest_framework import serializers
from visualizer import models as model


class Plant_Serializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = model.Plant
        fields = "__all__"

class Plant_information_Serializer(serializers.HyperlinkedModelSerializer):
    plant = Plant_Serializer(read_only=True)
    class Meta:
        model = model.Plant_information
        fields = "__all__"

class Energy_Serializer(serializers.HyperlinkedModelSerializer):
    plant_information = Plant_information_Serializer(read_only=True)
    class Meta:
        model = model.Energy
        fields = "__all__"

class Energy_Serializer_by_state(serializers.HyperlinkedModelSerializer):
    plant_information = Plant_information_Serializer(read_only=True)
    class Meta:
        model = model.Energy
        fields = "__all__"

class Energy_summary_Serializer(serializers.HyperlinkedModelSerializer):
    total_annual_net = serializers.DecimalField(max_digits=15,decimal_places=3, read_only=True)
    plant_information__plant__state = serializers.CharField(read_only=True)

    class Meta:
        model = model.Energy
        fields = ['total_annual_net','plant_information__plant__state']

class Data_year_Serializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = model.Energy
        fields = ['year']