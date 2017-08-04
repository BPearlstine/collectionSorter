from baseIndex import BaseIndex

class Book (BaseIndex):

    def __init__ (self,title, author, genre, date, isbn, edition):
        super(). __init__(title, author, genre, date)
        self.__isbn = isbn
        self.__edition = edition

    def __str__(self):

        return super().__str__() + ',' + str(self.__isbn) + ',' + self.__edition
