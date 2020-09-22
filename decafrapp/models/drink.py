from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Drink(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
