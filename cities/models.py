from django.db import models
from django.urls import reverse


class City(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        """Redirect after the make form to detail page."""
        return reverse('detail', kwargs={'pk': self.pk})
