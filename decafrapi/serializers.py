from rest_framework import serializers
from decafrapp.models import DrinkEntry, Entry, Drink

class DrinkEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = DrinkEntry
        fields = '__all__'
        depth = 2