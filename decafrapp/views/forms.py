from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from decafrapp.models import Entry, Drink

class RegistrationForm(UserCreationForm):
    
    class Meta: 
        model = User
        fields = ["username", "password1", "password2"]

class EntryForm(forms.ModelForm):
    class Meta: 
        model = Entry
        CHOICES = [
            ("verysad", "😢"),
            ("sad", "😕"),
            ("neutral", "😐"),
            ("happy", "🙂"), 
            ("veryhappy", "😁")
        ]
        fields=["mood", "notes"] 
        widgets = {
            "mood": forms.RadioSelect(choices=CHOICES),
            "notes": forms.Textarea()
        }

class DrinkEntryForm(forms.Form):
    drink = forms.ModelChoiceField(queryset=Drink.objects.all(), label="Drink")

class DrinkForm(forms.ModelForm):
    class Meta:
        model = Drink
        IMPACT_CHOICES = [
            ("1", "None"),
            ("2", "Mild"),
            ("3", "Normal"),
            ("4", "High"),
            ("5", "Severe"),
        ]
        TYPE_CHOICES = [
            ("tea", "Tea"),
            ("coffee", "Coffee"),
            ("softdrink", "Soft Drink"),
            ("enerygydrink", "Energy Drink"),
            ("shake", "Shake"),
            ("snack", "Snack Food"),
            ("medication", "OTC Medication")
        ]
        fields=["name", "caffeine_mg", "impact", "type"]
        widgets = {
            "impact": forms.RadioSelect(choices=IMPACT_CHOICES),
            "type": forms.Select(choices=TYPE_CHOICES)
        }
