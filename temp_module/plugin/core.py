
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
db = open("db", "r+")
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

Удалить ключ с значениме и вернуть да если удалил ложь если не удалил(если ключей было два) и ничего если ключа нет.


def core(link):  # Check if the file exists:
