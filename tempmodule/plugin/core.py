"""
    Я модуль и как правило я нужен для другорядных вещей
    таких как: дизайн текста(bg=black, color=white), язык текста
    (lang=EN), также я отвечаю за пользователя(log, pas)
"""

if __name__ == "__main__":  # If not imported, I exit is the module:
    print("I am is Module!!! Bye Bye!!!")
    exit()  # Answer: I'm leaving, I'm a module.


# db = open("db", "r+")
def bd_read(key: str) -> None:  # Вернуть содержимое по ключу или ничего если ключа нет
    return None  # value


def bd_create(key: str, value: str) -> None:  # Если ключа нет, добавить ключ с значением.
    pass


def bd_edit(key: str, value: str) -> None:  # Если ключ есть изменить его значение.
    pass


def bd_write(key: str, value: str) -> None:  # Записать в базу ключ с значением, Если ключ есть Заменить.
    pass


def bd_search(key: str) -> None:  # Вернуть первого нужного попавшигося ключа значение или ложь если не нашел.
    pass


def bd_check(key: str) -> None:  # Возвращает состояние есть ли ключ в базе.
    pass


# .Удалить ключ с значением и вернуть да если удалил ложь если не удалил(если ключей было два) и ничего если ключа нет.
# .Создать новый ключ с пустым значением. Вернуть да если создал, нет если уже есть ключ(ключи), ничего если(хз).

def core(command: list) -> None:  # Working with the database.
    if command[0] == "CREATE":  # Добавить елемент - Добавить ключ с значением в конец.
        """
            [TODO]
            f = open("bd", "a")
            f.append(f"[{command[1]} {command[2]}]\n")
            f.close()
        """

        f = open("bd")
        temp = str(f.read) + f"[{command[1]} {command[2]}]\n"
        f.close()

        f = open("bd", "w")
        f.write(temp)
        f.close()

        if command[0] == "UPDATE":  # Изменить элемент - Изменить первый попавшийся ключ.
            pass

        elif command[0] == "READER":  # Читать элемент - Читать первый попавшийся ключ.
            pass

        elif command[0] == "SEARCH":  # Искать элемент - Искать первый попавшийся ключ.
            pass

        elif command[0] == "DELETE":  # Удалить элемент - Убрать первый попавшийся ключ.
            pass

        elif command[0] == "NUMBER":  # Считать элемент - Узнать количество ключей
            pass
