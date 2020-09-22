from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DrinkEntrySerializer
from decafrapp.models import DrinkEntry

class DrinkEntryViewset(viewsets.ModelViewSet):
    serializer_class = DrinkEntrySerializer
    
    def get_queryset(self):
        user = self.request.user
        return DrinkEntry.objects.all().filter(user=user)
