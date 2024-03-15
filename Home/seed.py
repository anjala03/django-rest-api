from faker import Faker
from .models import *
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

def anotherfunc(n=5)->None:
    for _ in range(0,n):
        colors_purpos=["more_used", "less_used", "used_some_in_while"]
        color_cho=["red","green","blue", "white", "orange", "pink", "black", "violet"]
        color_name=random.choice(color_cho)
        color_used=random.choice(colors_purpos)
        color_code=f"CO-{random.randint(0,100)}"

        Colors.objects.create(
        color_name=color_name,
        color_used=color_used,
        color_code=color_code
        )
