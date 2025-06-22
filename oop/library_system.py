class Book:
    def __init__(self, title:str, author:str):
        self.title = title
        self.author = author

    def get_details(self):
        return f"Book: '{self.title}' by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def get_details(self):
        return f"E{super().get_details()} - {self.file_size}MB"

class PrintBook(Book):
    def __init__(self, title, author, page_count:int):
        super().__init__(title, author)
        self.page_count = page_count

    def get_details(self):
        return f"Print{super().get_details()} - {self.page_count} pages"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        
    def list_books(self):
        if not self.books:
            print("The library has no books.")
        else:
            for book in self.books:
                print(book.get_details())

