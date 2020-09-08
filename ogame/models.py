from django.db import models


class Planet(models.Model):
    galaxy = models.PositiveIntegerField(default=1)
    system = models.PositiveIntegerField(default=1)
    position = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.galaxy}:{self.system}:{self.position}'
