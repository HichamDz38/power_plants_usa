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
