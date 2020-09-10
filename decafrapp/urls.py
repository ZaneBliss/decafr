from django.urls import path
from .views import home

app_name = 'decafrapp'

urlpatterns = [
    path('', home, name='home')
]