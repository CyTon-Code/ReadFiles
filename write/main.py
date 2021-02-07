# Функция проверки файла (на редактирование и создание) перед работой с ним.
"""The module works only through import.
  Via os.system or return (RUN) - doesn't work."""

from check.main import check_file as check_file

error_code = 1


class ErrorCreate(Exception):
    def __init__(self):
        print(f"error: {error_code}")


if __name__ == "__main__":  # If not imported, I exit is the module:
    print("I am is Module!!! Bye Bye!!!")
    exit()  # Answer: I'm leaving, I'm a module.
    pass


def create_file(link):
    f = open(link, 'w')
    f.close()
    pass


# def


def write_file(link):  # Check if the file exists:
    """This module is required to read a file (or module).
    It can also check if a file (or module) exists."""
    # Credo: Checking the file for editable...

    file_open = True
    f = None

    try:  # Открываю файл или Создаю файл:
        f = open(link, 'w')

        if check_file(link):  # Если файла нет:
            # Я буду проверять на создание файла:
            try:  # Создаю файл:
                f = open(link, 'w')
                f.close()
                return False

            except:  # Не создал файл:
                file_open = False
                return None

            #     except:
            #       pass
            finally:
                try:  # Удаляю файл
                    from delete_file.main import delete_file
                    delete_file(link)

                except:  # Не удалил файл:
                    if file_open:  # If the file open:
                        raise ErrorCreate

            # TODO Нужно удалить за собой файл link
            file_open = False  # Нужно сказать что файл не открылся.
            return False  # Файл создать можно.

        else:  # Файл есть:
            # Я буду проверять на редактирование файла:
            try:  # записываю в файл:
                f.write('')
                return False

            except:  # Записать не получилось:
                return None

    except:  # Файл не открылся или не создался:
        print("f is not defined. f:", link)
        file_open = False

        return not file_open  # True

    finally:
        try:  # Закрываю файл:
            f.close()
            pass

        except:  # Файл не закрылся:
            if file_open:  # If the file open:
                raise ErrorEdit
    pass
