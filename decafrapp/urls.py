from django.urls import path, include
from . import views

app_name = 'decafrapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('logout', views.logout_view, name='logout'),
    path('newentry', views.entry, name='newentry')
]