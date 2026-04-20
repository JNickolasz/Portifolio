from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from decouple import config

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if not User.objects.filter(username=config('ADMIN_USER')).exists():
            User.objects.create_superuser(
                config('ADMIN_USER'),
                config('ADMIN_EMAIL'),
                config('ADMIN_PASSWORD')
            )
            self.stdout.write('Superusuário criado!')