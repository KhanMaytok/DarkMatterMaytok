import time
import winsound
from random import randint

from django.core.management import BaseCommand
from ogame import OGame
from ogame.constants import coordinates, status

from fleet.models import Planet


def login():
    return OGame('Yildun', 'khan@maytok.com', 'trolona')


def sos():
    for i in range(10):
        for x in range(0, 3):
            winsound.Beep(2000, 100)
        for y in range(0, 3):
            winsound.Beep(2000, 400)
        for z in range(0, 3):
            winsound.Beep(2000, 100)


def scan_inactives(empire):
    for galaxy in range(2, 7):
        for system in range(199, 500):
            # time.sleep(randint(3, 5))
            print(f'NOS ESTÁN ATACANDO???? {empire.attacked()}')
            if empire.attacked() is True:
                sos()
            for planet in empire.galaxy(coordinates(galaxy, system)):
                if status.inactive in planet.status and status.noob not in planet.status and status.vacation not in planet.status:
                    print('Find inactive')
                    print(planet.position)
                    Planet.objects.get_or_create(galaxy=galaxy, system=system, position=planet.position[2])


class Command(BaseCommand):
    help = 'Actualiza los numeros para nuevo método de conteo del siguiente'

    def handle(self, *args, **kwargs):
        # Planet.objects.all().delete()
        empire = login()
        scan_inactives(empire)
