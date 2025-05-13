from datetime import date

today = date.today()
year = int(today.strftime("%Y"))

class Book:
    def __init__(self, book_name, author, released, status):
        self.book_name = book_name
        if len(book_name) == 0:
            raise NameError("Назва книги не може бути пустою")
        self.author = author
        if len(author) == 0:
            raise NameError("Ім'я автора не може бути пустим")
        self.released = released
        if type(released) != int or released <=0 or released > year:
            raise ValueError(f"Рік випуску вказано в некоректному форматі: {self.released}")
        self. status = status

    def __str__(self):
        return f"{"-"*70}\n Назва книги: \"{self.book_name}\"\n Автор: {self.author}\n Рік випуску: {self.released}\n Статус: {self.status} \n"