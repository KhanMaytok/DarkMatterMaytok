import winsound

from django.core.management import BaseCommand
from ogame import OGame
from ogame.constants import coordinates, status

from fleet.models import Planet


def login():
    return OGame('Yildun', 'khan@maytok.com', 'trolona')


def sos():
    for i in range(0, 3):
        winsound.Beep(2000, 100)
    for i in range(0, 3):
        winsound.Beep(2000, 400)
    for i in range(0, 3):
        winsound.Beep(2000, 100)


def scan_inactives(empire):
    for galaxy in range(1, 7):
        print(f'NOS ESTÁN ATACANDO???? {empire.attacked()}')
        for system in range(1, 500):
            for planet in empire.galaxy(coordinates(galaxy, system)):
                if status.inactive in planet.status and status.noob not in planet.status and status.vacation not in planet.status:
                    print('Find inactive')
                    print(planet.position)
                    Planet.objects.get_or_create(galaxy=galaxy, system=system, position=planet.position[2])


class Command(BaseCommand):
    help = 'Actualiza los numeros para nuevo método de conteo del siguiente'

    def handle(self, *args, **kwargs):
        empire = login()
        scan_inactives(empire)
