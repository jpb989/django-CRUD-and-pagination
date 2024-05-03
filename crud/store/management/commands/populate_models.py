from faker import Faker
from django.core.management.base import BaseCommand
from store.models import Product, Brand

class Command(BaseCommand):
    help = 'Populate Product with fake data'
    name = "populate_models"

    def handle(self, *args, **kwargs):
        fake = Faker()
        #Populate Brand table
        for _ in range(10):
            Brand.objects.create(
                name=fake.company()
            )
        
        for _ in range(100):
            brand = Brand.objects.order_by("?").first()
            Product.objects.create(
                name = fake.word(),
                description = fake.text(),
                price = fake.random_number(digits=2),
                brand = brand
            )
        
        self.stdout.write(self.style.SUCCESS("Successfully populated Brand and Product models"))

    
    
        