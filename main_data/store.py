from faker import Faker
import random


fake = Faker('en_US')

order_dict=  {
  "id": fake.random_int(min= 1, max= 99999),
  "petId": fake.random_int(min= 1, max= 99999),
  "quantity": fake.random_int(min=1, max=9),
  "shipDate": fake.iso8601(tzinfo=None),
  "status": random.choice(["placed", "approved", "delivered"]),
  "complete": random.choice([True, False])
}

