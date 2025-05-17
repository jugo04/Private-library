from BooksStorage import BookStorage
from BookManager import BooksManager
from datetime import date

today = date.today()
year = int(today.strftime("%Y"))

manager = BooksManager()
storage = BookStorage()

main_menu = {
    1: "Додати книгу в бібліотеку",
    2: "Знайти книгу",
    3: "Кники в бібліотеці",
    4: "Завершити роботу"
}

book_menu = {
    1: "Змінити статус книги",
    2: "Видалити книгу",
    3: "До головного меню"
}

set_status_menu = {
    1: "Прочитано",
    2: "Почато",
    3: "Не почато"
}

continue_menu = {
    1: "Продовжити",
    2: "До головного меню"
}

find_menu = {
    1: "Пошку за назвою",
    2: "Пошук за автором"
}


def select(menu):
    for num, action in menu.items():
        print(num, action)
    choice = None
    while True:
        try:
            choice = int(input("Ваш вибір: "))
        except (ValueError, NameError):
            print("Команду вказано не вірно!")
            continue
        if choice <= 0 or choice > len(menu):
            print("Команду не знайдено!")
            continue
        break
    return choice

def set_status():
    status = None
    selected = select(set_status_menu)
    if selected == 1:
        status = "Прочитано"
    elif selected == 2:
        status = "Почато"
    elif selected == 3:
        status = "Не почато"
    return status

def manage(name):
    selected = select(book_menu)
    if selected == 1:
        new_status = set_status()
        manager.change_status(name, new_status)
    elif selected == 2:
        manager.delete_book(name)
    elif selected == 3:
        pass

def add_book():
    while True:
        name = input( "Назва книги: ")
        if  len(name) == 0:
            print("Назва книги не може бути пустою!")
            continue
        found = manager.find_book(name)
        if found:
            print(f"Книга \"{name}\" вже в бібліотеці")
            manage(found)
            break
        author = input("Автор книги: ")
        if len(author) == 0:
            print("Потрібно вказати автора книги!")
        try:
            realised = int(input("Рік випуску книги: "))
        except (ValueError, NameError):
            print("Рік випуску вказано в невірному форматі!")
            continue
        if realised > year:
            print("Рік випуску не може бути майбутнім")
            continue
        status = set_status()
        manager.create_book(name, author, realised, status)
        selected = select(continue_menu)
        if selected == 1:
            continue
        else:
            break

def find_book_for_name():
    search = input("Назва книги: ")
    found = manager.find_book(search)
    if found:
        print("Книгу знайдено")
        manager.show_book(found.book_name)
        manage(found)
    else:
        print("Книгу не знайдено")

def find_books_for_author():
    search = input("Ім'я автора: ")
    found = manager.find_for_author(search)
    if found:
        print("Книги автора в бібліотеці:")
        for book in found:
            manager.show_book(book.book_name)
    else:
        print("Автора не знайдено")

def find():
    while True:
        selected = select(find_menu)
        if selected == 1:
            find_book_for_name()
        elif selected == 2:
            find_books_for_author()
        else:
            break

while True:
    print("Головне меню:")
    command = select(main_menu)
    if command == 1:
        add_book()
    elif command == 2:
        find()
    elif command == 3:
        manager.show_books()
    elif command == 4:
        print("Роботу завершено")
        break

    #Потрібно додати пошук книги за автором
    # Можливість створення оцінки враження від книги