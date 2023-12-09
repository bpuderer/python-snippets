class Book:

    BOOK_TYPES = ('hardcover', 'paperback', 'ebook')

    def __init__(self, title, price, booktype):
        self.title = title
        self.price = price
        if booktype not in Book.BOOK_TYPES:
            raise ValueError(f'{booktype} in a valid type')
        else:
            self.booktype = booktype
        self.__secret = "this is a 'secret' attribute"

    def set_discount(self, amount):
        self._discount = amount  # leading _ denotes internal

    def get_price(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        return self.price

    @classmethod
    def get_book_types(cls):
        return Book.BOOK_TYPES

    @staticmethod      # required to call from instance of class
    def func_in_class():
        return "just a function hanging out in a class"



b1 = Book('a farewell to arms', 10, 'hardcover')
b1.set_discount(0.3)
print(b1.get_price())

b2 = Book('as i lay dying', 8, 'paperback')
print(b2.get_price())
# print(b2.__secret)  #AttributeError
print(b2._Book__secret)
print(Book.get_book_types())

print(type(b1))
print(isinstance(b1, Book))
print(isinstance(b1, object))

print(Book.func_in_class())
print(b1.func_in_class())
