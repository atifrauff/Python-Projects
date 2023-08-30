# creating library class which will store books in list and num. of books
class Library:
    def __init__(self):
        self.book = []
        self.numOfBooks = 0
    
# addbook method to add books into the list of class
    def addBook(self, bookk):
        self.book.append(bookk)
        self.numOfBooks = len(self.book)

# method to show total number of books library has
    def showInfo(self):
        print(f"The Library has {self.numOfBooks} books.\n")

# method to print out books in library individually with their index
    def showBooks(self):
        for index, i in enumerate(self.book, start=1):
            print(f"{index}- {i}")

# making first library by assigning it to a variable
l1 = Library()

# now adding books through addBook method created earlier
l1.addBook("Outliers")
l1.addBook("Think and Grow Rich")
l1.addBook("Rich Dad, Poor Dad")
l1.addBook("The Power of Now")
l1.addBook("The Power Introverts")

# calling the number of books using showInfo method created earlier 
l1.showInfo()
# calling all of the books using showBooks method created earlier
l1.showBooks()
