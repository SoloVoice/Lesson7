from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def calculation(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        self.calculation()

    def calculation(self):
        tissue_coat = round((self.size / 6.5 + 0.5), 1)
        print(f"Для пошива одного пальто требуется: {tissue_coat}м. ткани")


class Suit(Clothes):
    def __init__(self, height):
        self.height = height
        self.calculation()

    def calculation(self):
        tissue_suit = round((2 * self.height + 0.3), 1)
        print(f"Для пошива одного костюма требуется: {tissue_suit}м. ткани")


a = Coat(40)
b = Suit(1.78)
