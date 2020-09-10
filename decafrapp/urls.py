from django.urls import path, include
from .views import home

app_name = 'decafrapp'

urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls'))
]