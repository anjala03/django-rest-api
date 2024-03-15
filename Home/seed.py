from faker import Faker
from .models import People
import random

fake=Faker()
def afakerfunc(n=5)-> None:
    for _ in range(0,n):
        genders=['male', 'female', 'homosexual']
        person_name=fake.name()
        person_age=random.randint(0,50)
        person_gender=random.choice(genders)

        People.objects.create(
            name=person_name,
            age=person_age, 
            sex=person_gender
        )

