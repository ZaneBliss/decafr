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
        IMPACT_CHOICES = [
            ("none", "None"),
            ("mild", "Mild"),
            ("normal", "Normal"),
            ("high", "High"),
            ("severe", "Severe"),
        ]
        CHOICES = [
            ("😢", "😢"),
            ("😕", "😕"),
            ("😐", "😐"),
            ("🙂", "🙂"), 
            ("😁", "😁")
        ]
        fields=["mood", "impact", "notes"] 
        labels = {
            "impact": "Caffeine Impact"
        }
        widgets = {
            "mood": forms.RadioSelect(choices=CHOICES),
            "notes": forms.Textarea(),
            "impact": forms.RadioSelect(choices=IMPACT_CHOICES)
        }

class DrinkEntryForm(forms.Form):

    def __init__(self, user, *args, **kwargs):
        super(DrinkEntryForm, self).__init__(*args, **kwargs)
        self.fields['drink'] = forms.ModelChoiceField(queryset=Drink.objects.all().filter(user=user))

class DrinkForm(forms.ModelForm):
    class Meta:
        model = Drink
        TYPE_CHOICES = [
            ("tea", "Tea"),
            ("coffee", "Coffee"),
            ("softdrink", "Soft Drink"),
            ("enerygydrink", "Energy Drink"),
            ("shake", "Shake"),
            ("other", "Other"),
        ]
        fields=["name", "caffeine_mg", "type"]
        widgets = {
            "type": forms.Select(choices=TYPE_CHOICES)
        }
