from baseIndex import BaseIndex

class Card (BaseIndex):

    def __init__ (self, title, artist, genre, date, condition, foil):
        super().__init__(title, artist, genre, date)
        self.__condition = condition
        self.__foil = foil

    def __str__(self):

        return super().__str__() + ',' + self.__condition + ',' + self.__foil
