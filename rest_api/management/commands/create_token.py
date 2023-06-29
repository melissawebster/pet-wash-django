from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class Command(BaseCommand):
    help = 'Creates a new token to be used'
    def add_arguments(self, parser):
        parser.add_argument('--username', required=True)
        parser.add_argument('--password', required=True)

    def handle(self, *args, **options):
        username = options['username']
        password = options['password']

        self.stdout.write(
            self.style.WARNING(f'Creating user {username}')
        )
        user = User(username=username)
        user.first_name = username
        user.set_password(password)
        user.save()

        self.stdout.write(
            self.style.SUCCESS(f'User created') 
        )
        self.stdout.write(
            self.style.WARNING(f'Creating a token for the user...')
        )
        token = Token.objects.create(user=user)
        self.stdout.write(
            self.style.SUCCESS(f'Token created: {token.key}')
        )

