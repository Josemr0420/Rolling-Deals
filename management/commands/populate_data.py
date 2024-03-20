import random
from django.utils import timezone
from django.core.management.base import BaseCommand
from apps.auction import Hotwheel, Auction


class Command(BaseCommand):
    help = 'Llena los modelos de Django con datos de prueba'

    def handle(self, *args, **kwargs):
        # Crear instancias de Hotwheel
        hotwheels = [
            Hotwheel(model_name='Modelo A', year_released=2020, color='Rojo'),
            Hotwheel(model_name='Modelo B', year_released=2019, color='Azul'),
            Hotwheel(model_name='Modelo C', year_released=2021, color='Verde'),
        ]
        Hotwheel.objects.bulk_create(hotwheels)

        # Crear instancias de Auction
        for hotwheel in Hotwheel.objects.all():
            start_time = timezone.now()
            end_time = start_time + timezone.timedelta(days=random.randint(1, 30))
            Auction.objects.create(
                hotwheel=hotwheel,
                start_time=start_time,
                end_time=end_time,
                starting_bid=random.randint(10, 100),
            )

        self.stdout.write(self.style.SUCCESS('Datos de prueba creados exitosamente'))
