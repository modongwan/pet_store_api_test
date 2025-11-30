from faker import Faker
import random

fake = Faker('en_US')

pet_dict=  {
    "id": fake.random_int(min=1, max=999999),
    "category": {
        "id": fake.random_int(min=1, max=99999),
        "name": random.choice(["dog","cat","hamster"])
    },
    "name": fake.first_name(),
    "status":  random.choice(["available", "sold", "pending"] )
}