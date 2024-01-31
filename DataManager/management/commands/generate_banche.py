from django.core.management.base import BaseCommand
from ...models.artico import Artico  # Import your Banche model
from Login.models import CustomUser
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Creates 100,000 random instances of Banche model'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Get all users in the database
        users = CustomUser.objects.all()

        for i in range(999999):
            # Generate random data for the Banche model
            random_instance = Artico(
                codart=i,
                desart='des ' + str(i),
                prezzo=fake.random_number(digits=5),
                user=random.choice(users),
            )
            random_instance.save()
