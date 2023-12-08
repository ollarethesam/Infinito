from django.core.management.base import BaseCommand
from ...models.banche import Banche  # Import your Banche model
from django.contrib.auth.models import User
from faker import Faker
from datetime import datetime
import random

class Command(BaseCommand):
    help = 'Creates 100,000 random instances of Banche model'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Get all users in the database
        users = User.objects.all()

        for i in range(999):
            # Generate random data for the Banche model
            random_instance = Banche(
                codban=str(i).zfill(3),
                desban=str(i).zfill(5),
                codabi=fake.random_number(digits=5),
                codcab=fake.random_number(digits=5),
                codsia=fake.random_number(digits=5),
                iban=fake.iban(),
                bic=fake.swift(),
                user=random.choice(users),
                date_created=fake.date_time_between(start_date='-1y', end_date='now')
            )
            random_instance.save()
