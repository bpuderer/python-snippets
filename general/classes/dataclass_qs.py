from dataclasses import dataclass, field
import random


def price_func():
    return float(random.randrange(5, 10))

@dataclass
class Book:
    title: str
    author: str = "No author"
    #price: float = field(default=10.0)
    price: float = field(default_factory=price_func)


    def __post_init__(self):
        self.description = f'{self.title} by {self.author}'

@dataclass(frozen=True)
class ImmutableClass:
    value1: str = "val1"
    value2: int = 0


b1 = Book("A Fable", "Faulkner")
b2 = Book("A Fable", "Faulkner")
b3 = Book("As I Lay Dying", "Faulkner")
b4 = Book('unknown')

print(b1)
print(b4)
print(b1 == b2)
print(b1 == b3)

print(b1.price)
print(b1.description)

ic1 = ImmutableClass()
#ic1.value1 = "blah"  # raises FrozenInstanceError


