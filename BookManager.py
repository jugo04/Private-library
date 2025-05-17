from Book import Book
from BooksStorage import BookStorage

class BooksManager:
    def __init__(self):
        self.books = BookStorage()
        self.storage = self.books.load_file()

    def find_book(self,name):
        for book in self.storage:
            if book.book_name.lower() == name.lower():
                return book
        return None

    def find_by_author(self, author):
        find_books = []
        for book in self.storage:
            if book.author.lower() == author.lower():
                find_books.append(book)
        return find_books

    def create_book(self, name, author, released, status):
        new_book = Book(name, author, released, status)
        self.storage.append(new_book)
        print("Книгу створено")
        self.books.save_to_file(self.storage)

    def delete_book(self, name):
        if name:
            self.storage.remove(name)
            print (f"Книгу видалено: {name.book_name}")
            self.books.save_to_file(self.storage)
        else:
            print(f"Книга \"{name}\" відсутня в бібліотеці")

    def change_status(self, name, new_status):
        name.status = new_status
        self.books.save_to_file(self.storage)
        print(f"Статус книги змінено на \"{new_status}\"")

    def show_book(self, name):
        found = self.find_book(name)
        if found:
            print(found)
        else:
            print("Книга відсутня в бібліотеці")

    def show_books(self):
        if self.storage:
            print("Книги в бібліотеці:")
            for book in self.storage:
                print(book)
        else:
            print("Бібліотека пуста")