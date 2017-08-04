from baseIndex import BaseIndex
from book import Book
from comic import Comic
from card import Card

#function for writing object to csv
def writeFile (filename, object):
    output_file = open (filename, 'a')
    strObj = str(object) + '\n'
    output_file.write (strObj)

    output_file.close()

#function for creating book object
def addBook():
    bookLibrary = "bookLibrary.csv"

    itemName = input("Enter book name: ")
    itemAuthor = input("Enter book's author: ")
    itemType = input("Enter book genre: ")
    itemPublished = input("Enter book's publication date: ")
    itemISBN = input("Enter the book's ISBN: ")
    itemEdition = input("Is the book first edition: ")

    createBook = Book(itemName,itemAuthor,itemType,itemPublished, itemISBN, itemEdition)
    writeFile (bookLibrary, createBook)

#function for adding comic object
def addComic():
    comicLibrary = "comicLibrary.csv"

    itemName = input("Enter comic name: ")
    itemCreators = input("Enter comic's writer and artist: ")
    itemType = input("Enter comic's publisher: ")
    itemPublished = input("Enter comic's publication date: ")
    itemIssue = input("Enter the comic's issue: ")
    itemVariant = input("Is the comic a variant?: ")

    createComic = Comic(itemName,itemCreators,itemType,itemPublished, itemIssue, itemVariant)
    writeFile (comicLibrary, createComic)

#function for adding card object
def addCard():
    cardLibrary = "cardLibrary.csv"

    itemName = input("Enter card name: ")
    itemArtist = input("Enter card's artist: ")
    itemSet = input("Enter card Set: ")
    itemPublished = input("Enter card print date: ")
    itemCondition = input("Enter the card's condition: ")
    itemFoil = input("Is the card a foil?: ")

    createCard = Card(itemName,itemArtist,itemSet,itemPublished, itemCondition, itemFoil)
    writeFile (cardLibrary, createCard)

def searchFunc (objType):
    searchTerm = input("Search: ")
    if objType == "books":
        with open("bookLibrary.csv") as forSearch:
            for row in forSearch:
                if  searchTerm in row:
                    print (row)
    elif objType == "comics":
        with open("comicLibrary.csv") as forSearch:
            for row in forSearch:
                if  searchTerm in row:
                    print (row)
    else:
        with open("cardLibrary.csv") as forSearch:
            for row in forSearch:
                if  searchTerm in row:
                    print (row)

def main():
    keepRunning = "yes"
    contAdd = "no"
    contSearch = "no"
    while keepRunning == "yes"
        print ("Enter 'add' to enter a new item to your library")
        print ("Enter 'search' to search your library.")
        choice = input(": ")
        if choice == "add":
            contAdd = "yes"
        elif choice == "search":
            contSearch = "yes"
        else:
            contChange = "yes"
        while contAdd == "yes":
            medium = input("what medium are you entering? book, comic, or card?: ")
            if medium == "book":
                addBook()

            elif medium == "comic":
                addComic()

            else:
                addCard()

            contAdd =input("Do you want to add another item to your library?(yes/no): ")
        while contSearch == "yes":
            forSearch = input ("Do you want to search your books, comics, or cards? ")
            searchFunc(forSearch)
            contSearch = input("Do you want to do another search? ")

main()
