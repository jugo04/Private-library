import json
from Book import Book

class BookStorage:
    @staticmethod
    def convert_to_dict(books):
        books_list = []
        for book in books:
            books_dict = {
                "book_name": book.book_name,
                "author": book.author,
                "released": book.released,
                "status": book.status
            }
            books_list.append(books_dict)
        return books_list

    @staticmethod
    def convert_to_list(books):
        book_list = []
        for book in books:
            converted_book = Book(
                book["book_name"], book["author"], book["released"], book["status"]
            )
            book_list.append(converted_book)
        return book_list

    def load_file(self):
        try:
            with open("library.json", "r", encoding="utf-8") as read_file:
                loaded = json.load(read_file)
            convert = self.convert_to_list(loaded)
            return convert
        except Exception as e:
            print(f"Не вдалось прочитати файл: {e}")
            return []

    def save_to_file(self, books):
        try:
            book_to_save = self.convert_to_dict(books)
            with open("library.json", "w", encoding="utf-8") as save_file:
                json.dump(book_to_save, save_file, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Не вдалося додати дані до файлу: {e}")