from django.core.exceptions import ValidationError
from django.db import models

from cities.models import City
from trains.models import Train


class Route(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Name of route')
    travel_time_total = models.PositiveIntegerField(verbose_name='Total time in travel')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='route_from_city_set')
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='route_to_city_set')
    trains = models.ManyToManyField(Train, verbose_name='List of train')

    def __str__(self):
        return f'Route #{self.name} from {self.from_city} to {self.to_city}'

    class Meta:
        ordering = ['travel_time_total']
