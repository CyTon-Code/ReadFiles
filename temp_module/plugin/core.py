
"""Я модуль и как правило я нужен для другорядных вещей
таких как: дизайн текста(bg=black, color=white), язык текста
(lang=EN), также я отвечаю за пользователя(log, pas)"""
error_code = 1


class FileDidNotClose(Exception):
    def __init__(self):
        print(f"error: {error_code}")


if __name__ == "__main__":  # If not imported, I exit is the module:
    print("I am is Module!!! Bye Bye!!!")
    exit()  # Answer: I'm leaving, I'm a module.
    pass
# db = open("db", "r+")
def bd_read(key):  # Вернуть содержимое по ключу или ничего если ключа нет
    return None#value

def bd_create(key, value):  # Если ключа нет, добавить ключ с значением.
    pass

def bd_edit(key, value):  # Если ключ есть изменить его значение.
    pass

def bd_write(key, value):  # Записать в базу ключ с значением, Если ключ есть Заменить.
    pass

def bd_search(key):  # Вернуть первого нужного попавшигося ключа значение или ложь если не нашел.
    pass

def bd_check(key):  # Возвращает состояние есть ли ключ в базе.
    pass

# .Удалить ключ с значением и вернуть да если удалил ложь если не удалил(если ключей было два) и ничего если ключа нет.
# .Создать новый ключ с пустым значением. Вернуть да если создал, нет если уже есть ключ(ключи), ничего если(хз).

def core(command:list):  # Working with the database.
    if command[ 0 ] == "CREATE":  # Добавить елемент - Добавить ключ с значением в конец.
        pass
    elif command[0] == "UPDATE":  # Изменить элемент - Изменить первый попавшийся ключ.
        pass
    elif command[0] == "READER":  # Читать элемент - Читать первый попавшийся ключ.
        pass
    elif command[0] == "SEARCH":  # Искать элемент - Искать первый попавшийся ключ.
        pass
    elif command[0] == "DELETE":  # Удалить элемент - Убрать первый попавшийся ключ.
        pass
    elif command[0] == "NUMBER":  # Считать элемент - Узнать количество ключей
        pass
#     i = ["U", "R"]
#     if command[0] in i:  # Update / Rename
#         pass
#     i = ["D"]
#     if command[0] in i:  # Delete
#         pass
#     "C"
#     elif command[0] == :  # Create \ New
#         pass
#     elif command[0] == "S":  # Search
#         pass
#     else:
#         pass
#     pass
