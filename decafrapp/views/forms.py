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
        CHOICES = [
            ("verysad", "😢"),
            ("sad", "😕"),
            ("neutral", "😐"),
            ("happy", "🙂"), 
            ("veryhappy", "😁")
        ]
        model = Entry
        fields=["mood", "notes"] 
        widgets = {
            "mood": forms.RadioSelect(choices=CHOICES),
            "notes": forms.Textarea()
        }

class DrinkEntryForm(forms.Form):
    drink = forms.ModelChoiceField(queryset=Drink.objects.all(), label="Drink")
