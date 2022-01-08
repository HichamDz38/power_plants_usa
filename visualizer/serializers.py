from rest_framework import serializers

from visualizer import models as model

cities = {
    "AL": "Alabama",
    "AK": "Alaska",
    "AS": "American Samoa",
    "AZ": "Arizona",
    "AR": "Arkansas",
    "CA": "California",
    "CO": "Colorado",
    "CT": "Connecticut",
    "DE": "Delaware",
    "DC": "District Of Columbia",
    "FM": "Federated States Of Micronesia",
    "FL": "Florida",
    "GA": "Georgia",
    "GU": "Guam",
    "HI": "Hawaii",
    "ID": "Idaho",
    "IL": "Illinois",
    "IN": "Indiana",
    "IA": "Iowa",
    "KS": "Kansas",
    "KY": "Kentucky",
    "LA": "Louisiana",
    "ME": "Maine",
    "MH": "Marshall Islands",
    "MD": "Maryland",
    "MA": "Massachusetts",
    "MI": "Michigan",
    "MN": "Minnesota",
    "MS": "Mississippi",
    "MO": "Missouri",
    "MT": "Montana",
    "NE": "Nebraska",
    "NV": "Nevada",
    "NH": "New Hampshire",
    "NJ": "New Jersey",
    "NM": "New Mexico",
    "NY": "New York",
    "NC": "North Carolina",
    "ND": "North Dakota",
    "MP": "Northern Mariana Islands",
    "OH": "Ohio",
    "OK": "Oklahoma",
    "OR": "Oregon",
    "PW": "Palau",
    "PA": "Pennsylvania",
    "PR": "Puerto Rico",
    "RI": "Rhode Island",
    "SC": "South Carolina",
    "SD": "South Dakota",
    "TN": "Tennessee",
    "TX": "Texas",
    "UT": "Utah",
    "VT": "Vermont",
    "VI": "Virgin Islands",
    "VA": "Virginia",
    "WA": "Washington",
    "WV": "West Virginia",
    "WI": "Wisconsin",
    "WY": "Wyoming"
}


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

class Energy_Serializer_sum(serializers.HyperlinkedModelSerializer):
    plant_information = Plant_information_Serializer(read_only=True)
    class Meta:
        model = model.Energy
        fields = ("plant_information","generator_anual_net")