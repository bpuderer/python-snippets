from abc import ABC, abstractmethod


# abstract base class
class Shape(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def calc_area(self):
        pass


class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass


class Circle(Shape, JSONify):
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        return 3.14 * (self.radius ** 2)

    def toJSON(self):
        return f'{{"Circle": {self.calc_area()}}}'


c1 = Circle(2.8)
print(f'area if circle of radius {c1.radius} = {c1.calc_area()}')
print(c1.toJSON())
