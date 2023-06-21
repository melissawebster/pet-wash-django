from django.core.management.base import BaseCommand
from model_bakery import baker
from booking.models import Booking

class Command(BaseCommand):
    help = 'create fake data to test API'
    def handle(self, *args, **options):
        total = 50
        self.stdout.write(
            self.style.WARNING(f'Creating {total} bookings')
        )
        for i in range(total):
            booking = baker.make(Booking)
            booking.save()
        self.stdout.write(
            self.style.SUCCESS('Bookings created')
        )