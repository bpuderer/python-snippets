# PEP 435
# https://docs.python.org/3.7/library/enum.html#module-enum
from enum import Enum


# members are hashables, singletons
class Animal(Enum):
    # WALLABY = auto()   # if val is unimportant
    WALLABY = 1
    STEER = 2
    TURTLE = 3
    DOG = 4

for animal in Animal:
    print(animal, animal.name, animal.value)

pet = Animal.DOG
# Enumeration members are compared by identity...they are singletons - PSF
print(pet is Animal.DOG)
print(Animal['TURTLE'], Animal(3))
