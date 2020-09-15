from django.db import models
from django.urls import reverse
from .drink import Drink
from .entry import Entry

class DrinkEntry(models.Model):

    drink = models.ForeignKey(Drink, on_delete=models.DO_NOTHING)
    entry = models.ForeignKey(Entry, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = ("DrinkEntry")
        verbose_name_plural = ("DrinkEntrys")

    def get_absolute_url(self):
        return reverse("DrinkEntry_detail", kwargs={"pk": self.pk})
