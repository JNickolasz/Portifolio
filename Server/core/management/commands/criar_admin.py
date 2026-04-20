from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='josenickolas').exists():
            User.objects.create_superuser('josenickolas', os.environ.get('EMAIL_ADDRESS'), 'sitoio7593')
            self.stdout.write('Superusuário criado!')