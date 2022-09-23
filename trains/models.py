from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse

from cities.models import City


class Train(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Number the train')
    travel_time = models.PositiveIntegerField(verbose_name='Time in travel')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='from_city_set')
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='to_city_set')

    def __str__(self):
        return f'Train #{self.name} from {self.from_city} to {self.to_city}'

    class Meta:
        ordering = ['travel_time']

    def clean(self):
        """The doing a check data before save to DB."""
        if self.from_city == self.to_city:
            raise ValidationError('Please change city!')
        qs = Train.objects.filter(
            from_city=self.from_city,
            to_city=self.to_city,
            travel_time=self.travel_time).exclude(pk=self.pk)

        if qs.exists():
            raise ValidationError('Please change the travel time!')

    def save(self, *args, **kwargs):
        """The rewrite method save()"""
        self.clean()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Redirect after the make form to detail page."""
        return reverse('trains:detail', kwargs={'pk': self.pk})
