# Функция проверки файла (на редактирование и создание) перед работой с ним.
"""The module works only through import.
  Via os.system or return (RUN) - doesn't work."""


class ErrorCreate(Exception):
    pass


if __name__ == "__main__":  # If not imported, I exit is the module:
    print("I am is Module!!! Bye Bye!!!")
    exit()  # Answer: I'm leaving, I'm a module.
    pass


def create_file(AddressFile):
    f = open(AddressFile, 'w')
    f.close()
    pass


# def
from check_file.main import check_file as check_file


def write_file(address_file):  # Check if the file exists:
    """This module is required to read a file (or module).
    It can also check if a file (or module) exists."""
    # Сredo: Checking the file for editable...

    file_open = True
    try:  # Открываю файл или Создаю файл:
        File = open(address_file, 'w')

        if check_file(address_file):  # Если файла нет:
            # Я буду проверять на создание файла:
            try:  # Создаю файл:
                f = open(address_file, 'w')
                f.close()
                return False

            except:  # Не создал файл:
                FileOPn = False
                return None

            #     except:
            #       pass
            finally:
                try:  # Удаляю файл
                    from delete_file.main import delete_file
                    delete_file(address_file)

                except:  # Не удалил файл:
                    if file_open:  # If the file open:
                        raise ErrorCreate

            # TODO Нужно удалить за собой файл link
            file_open = False  # Нужно сказать что файл не открылся.
            return False  # Файл создать можно.

        else:  # Файл есть:
            # Я буду проверять на редактирование файла:
            try:  # записываю в файл:
                File.write('')
                return False

            except:  # Записать не получилось:
                return None

    except:  # Файл не открылся или не создался:
        print("File is not defined. File:", address_file)
        file_open = False

        return not file_open  # True

    finally:
        try:  # Закрываю файл:
            File.close()
            pass

        except:  # Файл не закрылся:
            if file_open:  # If the file open:
                raise ErrorEdit
    pass
