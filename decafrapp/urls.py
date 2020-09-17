from django.urls import path, include
from . import views

app_name = 'decafrapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('logout', views.logout_view, name='logout'),
    path('entries', views.entry_list, name='entries'),
    path('entries/<int:pk>', views.entry_detail, name='entry'),
    path('drinks', views.drink_list, name='drinks'),
    path('dirnks/<int:pk>', views.drink_detail, name='drink'),
    path('newentry', views.entry_form, name='newentry'),
    path('newdrink', views.drink_form, name='newdrink')
]