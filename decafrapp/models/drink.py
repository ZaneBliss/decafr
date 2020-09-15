from django.db import models
from django.urls import reverse

class Drink(models.Model):

    name = models.CharField(max_length=50)
    caffeine_mg = models.DecimalField(decimal_places=1, max_digits=5)
    type = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Drink")
        verbose_name_plural = ("Drinks")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Drink_detail", kwargs={"pk": self.pk})
