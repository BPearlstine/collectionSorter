class BaseIndex:

    def __init__ (self, title, creator, type, date):
        self.__id = title
        self.__creator = creator
        self.__media = type
        self.__published = date

    def __str__ (self):

        csvStr = self.__id + ',' + self.__creator + ',' + self.__media \
                 + ',' + str(self.__published)

        return csvStr
