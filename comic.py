from baseIndex import BaseIndex

class Comic (BaseIndex):

    def __init__ (self, title, creators, genre, date, issue, variant):
        super(). __init__(title, creators, genre, date)
        self.__issue = issue
        self.__variant = variant

    def __str__(self):

        return super().__str__() + ',' + str(self.__issue) + ',' + self.__variant
