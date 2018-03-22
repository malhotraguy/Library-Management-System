class library:
    def __init__(self,ListOfBooks):
        self.availableBooks=ListOfBooks
# Layers of Abstraction => to display all books, to lend book , to add book
    def DisplayBooks(self):
        print()
        print("Available Books:")
        n=1
        for book in self.availableBooks:
            print(n,")",book)
            n+=1
        print()
    def LendBook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print("Book you requested ",requestedBook,"has been issued to you!!")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry this book is not available!!")

    def AddBook(self,returnedBook):
        self.availableBooks.append(returnedBook)


class customer:
#layers of abstraction => to request a book, return a book
    def ReqBook(self):
        print("Enter the name of book you want?!!")
        self.Book= input()
        return self.Book
    def ReturnBook(self):
        print("Enter the name of the book you want to return!!")
        self.Book=input()
        return self.Book

Library=library(["Monk who sold his ferrari","Revolution 2020","The Alchemist","Happiness is not so Expensive"])
Customer= customer()
while True:
    print("Enter 1 to display the available books ")
    print("Enter 2 to request for a book ")
    print("Enter 3 to return a book ")
    print("Enter 4 to exit")
    userChoice = input()
    if userChoice == "1":
        Library.DisplayBooks()
    elif userChoice == "2":
        Customer.ReqBook()
        Library.LendBook(Customer.Book)
    elif userChoice == "3":
        RBook=Customer.ReturnBook()
        if RBook1\
                in Library.availableBooks:
            print("Your Book has been already been returned!. So cant take it again!!")
            print()
        else:
            Library.AddBook(Customer.Book)
            print("Your book has been returned!!")
    elif userChoice == "4":
        quit()
    else:
        print("Invalid Input")
