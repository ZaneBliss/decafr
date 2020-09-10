from django.db import models
from django.urls import reverse

class Entry(models.Model):

    mood = models.CharField(max_length=50)
    notes = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Entry")
        verbose_name_plural = ("Entrys")

    def __str__(self):  
        return self.name

    def get_absolute_url(self):
        return reverse("Entry_detail", kwargs={"pk": self.pk})
