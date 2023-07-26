# Code to raffle a client to receive a free bath

from django.core.management.base import BaseCommand, CommandParser
from booking.models import Branch
import random


class Command(BaseCommand):
    def list_branches(self):
        return Branch.objects.all().values_list('pk', flat=True)
    
    def add_arguments(self, parser):
        parser.add_argument(            
            'quantity', # means flag
            nargs = '?', # means not mandatory
            default=5, # if user doesnt specify quantity, it gets 5 by default
            type=int,
            help='How many clients can participate?'
        )
        parser.add_argument(            
            '-branch',
            required=True,
            type=int,
            choices=self.list_branches(),
            help='Type the ID of the branch to run the raffle'
        )

    def choose_bookings(self, baths, quantity):
        baths_list = list(baths)
        if quantity > len(baths_list):
            quantity = len(baths_list)
        return random.sample(baths_list, quantity)
    
    def print_chosen_baths(self, baths):
        self.stdout.write()
        self.stdout.write(
            self.style.HTTP_INFO('Dados das pessoas e animais sorteados')
        )
        self.stdout.write(self.style.HTTP_INFO('='*35))
        
        for bath in baths:
            self.stdout.write(self.style.HTTP_INFO(f'Pet: {bath.pet_name}'))
            self.stdout.write(self.style.HTTP_INFO(f'Tutor: {bath.name}'))
            self.stdout.write(self.style.HTTP_INFO('='*35))

    def print_info_petshop(self, branch):
        self.stdout.write(
            self.style.HTTP_INFO(
                'Infos about the branch who ran the promo'
            )
        )
        self.stdout.write(f'Branch name: {branch.name}')
        self.stdout.write(f'Address: {branch.street}, {branch.street_number}')

    def handle(self, *args, **options):
        quantity = options['quantity']
        branch_id = options['branch']

        branch = Branch.objects.get(pk=branch_id)
        bookings = branch.branch.all()
        chosen_baths = self.choose_bookings(bookings, quantity)

        self.stdout.write(
            self.style.SUCCESS('Sorteio realizado')
        )
        self.print_info_petshop(branch)
        self.print_chosen_baths(chosen_baths)




        