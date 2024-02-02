"""
Create an app that:

It would have a class Person, with properties name and age
The class would have a repr method that would render the name and age
Initialize multiple Person objects with names and ages
Add created Human objects to a new list
Sort and print list objects by name and age (and vice versa)
Advices:

Use sorted, attrgetter, reverse, function repr
from operator import attrgetter
"""

from operator import attrgetter


# 4.1
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 4.2
    def __repr__(self):
        return f"{self.name}. {self.age}."


# 4.3

human1 = Human("Aark", 45)
human2 = Human("Bohn", 92)
human3 = Human("Coel", 32)
human4 = Human("Dess", 35)

# 4.4
human_list = [human4, human3, human2, human1]

# 4.5
print(sorted(human_list, key=lambda x: x.name))
print(sorted(human_list, key=lambda x: x.name, reverse=True))
print(sorted(human_list, key=lambda x: x.age))
print(sorted(human_list, key=lambda x: x.age, reverse=True))

print(sorted(human_list, key=attrgetter("name")))
print(sorted(human_list, key=attrgetter("age")))
