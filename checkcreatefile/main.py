"""The module works only through import.
  Via os.system or return (RUN) - doesn't work."""
from delete_file.main import delete_file

error_code = 3


class ErrorClearFile(Exception):
    def __init__(self):
        print(f"error: {error_code}. ")


class ErrorExitFile(Exception):
    def __init__(self):
        print(f"error: {error_code}")


if __name__ == "__main__":  # If not imported, I exit is the module:
    print("I am is Module!!! Bye Bye!!!")
    exit()  # Answer: I'm leaving, I'm a module.


def check_create_file(link):  # Check if the f is being created:
    """This module is required to create a f (or module)."""
    # Credo: Checking the f for editable...

    # Решение проблемы с закрытием файлов, которые не открывались:
    file_open = True
    f = None

    try:  # Создаю файл:
        f = open(link, 'x')
        return False

    except FileExistsError:  # Файл не создался:
        file_open = False
        return True

    finally:
        try:  # Закрываю файл:
            f.close()
            if delete_file(link) is None:  # Удаляю файл:
                raise ErrorClearFile

        except:  # Файл не закрылся:
            if file_open:  # If the f open:
                raise ErrorExitFile
