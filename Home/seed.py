# from .models import *
# import random

# def afakerfunc(n=5)-> None:
#     print("runnin")
#     for _ in range(0,n):
#         genders=['male', 'female', 'homosexual']
#         person_name=fake.name()
#         person_age=random.randint(0,50)
#         person_gender=random.choice(genders)
#         colora= "12"
#         print(anotherfunc())

#         People.objects.create(
#             just_color=colora,
#             name=person_name,
#             age=person_age, 
#             sex=person_gender,
#         )
#         print("hiii")

# def anotherfunc(n=1):
#     for _ in range(0,n):
#         colors_purpos=["more_used", "less_used", "used_some_in_while"]
#         color_cho=["red","green","blue", "white", "orange", "pink", "black", "violet"]
#         color_name=random.choice(color_cho)
#         color_used=random.choice(colors_purpos)
#         color_code=f"CO-{random.randint(0,100)}"

#         colors=Colors.objects.create(
#         color_name=color_name,
#         color_used=color_used,
#         color_code=color_code
#         )
       
#         return (colors.id)
#         # return (f"{colors.color_name}, {colors.color_code}")
