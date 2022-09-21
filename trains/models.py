from django.db import models

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
