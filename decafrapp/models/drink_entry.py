from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from .drink import Drink
from .entry import Entry

class DrinkEntry(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE, related_name='drink')
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name='entry')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("DrinkEntry")
        verbose_name_plural = ("DrinkEntrys")

    def get_absolute_url(self):
        return reverse("DrinkEntry_detail", kwargs={"pk": self.pk})
