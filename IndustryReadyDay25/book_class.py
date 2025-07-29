"""Make a Book class with title, author, and year
Add methods to display the book info and one using __str__()
Create 2 books and print them"""
class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
    def __str__(self):
        return f"Book Title: {self.title} Written by: {self.author} in {self.year}"
book=Book("1984", "George Orwell", 1949)
print(book)
book2=Book("To Kill a Mockingbird", "Harper Lee", 1960)
print(book2)
    