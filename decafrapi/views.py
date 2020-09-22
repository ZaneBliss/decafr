from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DrinkEntrySerializer
from decafrapp.models import DrinkEntry

class DrinkEntryViewset(viewsets.ModelViewSet):
    queryset = DrinkEntry.objects.all()
    serializer_class = DrinkEntrySerializer