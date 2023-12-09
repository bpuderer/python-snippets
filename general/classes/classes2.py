# example from PluralSight Python - Beyond the Basics
import random


class ShippingContainer:

    next_serial = 283
    HEIGHT_FT = 8.5
    WIDTH_FT = 8.0

    @staticmethod
    def _make_code(owner, serial):
        return f'{owner}{serial}-{str(random.randint(0, 1000)).zfill(6)}'

    @classmethod
    def _get_next_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    # named constructor, aka factory function
    @classmethod
    def create_empty(cls, owner_code, length_ft, *args, **kwargs):
        return cls(owner_code, length_ft, contents=None, *args, **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, length_ft, contents, *args, **kwargs):
        return cls(owner_code, length_ft, contents=list(contents), *args, **kwargs)

    def __init__(self, owner_code, length_ft, contents):
        self.owner_code = owner_code
        self.length_ft = length_ft
        self.contents = contents
        # would not use overridden _make_code
        #self.serial = ShippingContainer._make_code(owner_code, ShippingContainer._get_next_serial())
        self.code = self._make_code(owner_code, ShippingContainer._get_next_serial())

    @property
    def volume_ft3(self):
        return (ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.length_ft)

    def __str__(self):
        return f'owner_code: {self.owner_code}  length_ft: {self.length_ft}  vol: {self.volume_ft3}  contents: {self.contents}  serial: {self.code}'


class RefridgeratedContainer(ShippingContainer):
    
    MAX_TEMP = 5.0
    FRIDGE_VOLUME_FT3 = 100

    @staticmethod
    def _make_code(owner, serial):
        return f'ZZZ{owner}{serial}-{str(random.randint(0, 1000)).zfill(6)}'
    
    def __init__(self, owner_code, length_ft, contents, temperature):
        super().__init__(owner_code, length_ft, contents)
        self.temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value > RefridgeratedContainer.MAX_TEMP:
            raise ValueError('Temp is too high!')
        self._temperature = value

    def __str__(self):
        return f'owner_code: {self.owner_code}  length_ft: {self.length_ft}  vol: {self.volume_ft3}  contents: {self.contents}  serial: {self.code}  temperature: {self.temperature}'

    @property
    def volume_ft3(self):
        return (super().volume_ft3 - RefridgeratedContainer.FRIDGE_VOLUME_FT3)


class HeatedRefridgeratedContainer(RefridgeratedContainer):

    MIN_TEMP = -5.0

    # overriding property setter more involved than overriding getter
    @RefridgeratedContainer.temperature.setter
    def temperature(self, value):
        if value < HeatedRefridgeratedContainer.MIN_TEMP:
            raise ValueError('Temp is too cold!')
        # super().temperature = value
        RefridgeratedContainer.temperature.fset(self, value)



if __name__ == '__main__':
    sc = ShippingContainer('ABC', 15, 'apples')
    print(sc)
    rc = RefridgeratedContainer('ABC', 20, 'oranges', temperature=2.0)
    print(rc)
    # polymorphic class method
    rc2 = RefridgeratedContainer.create_empty('ABC', 15, temperature=-44.0)
    print(rc2)
    hrc = HeatedRefridgeratedContainer('XYX', 20, 'stuffs', temperature=-5.0)
    print(hrc)
