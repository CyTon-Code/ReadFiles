import os
from whats_file_name import whats_file_name
from check_file.main import check_file


def equal(a: str, b: str):
    return a == b


def moving_a_file(link: str, path="work/moving_a_file.py"):
    """
    функция которая перемещает модули между ворк и хранилием в реад...
    Cut:
    .переменстить файл
    .сохранить имя а точнее первый адресс.
    .переименоать в либ.
     .при переподключении к другому модулю:
      .переметстить назад и вернуть имя.
      .начать с нулевого пункта.
     .при подключении к тому же самому модулю:
      .ничего не менять.
    .подключить модуль.
    """
    # TO DO: Нужно доработать проверку разности имен, а также проверку
    # на сущестование файла перед перемещением.
    if equal(link, path) or not equal(whats_file_name(link),
                                      whats_file_name(path)):
        # Также сюда нужно попасть когда имена в адресах не
        # совпадают нельзя перемещать переименовывая файл.
        # адресса совпадают: перемещать не нужно.
        return True
    else:  # Перемещаем и переменовываем файл:
        if check_file(link):  # if (os.path.exists(link)):
            os.replace(link, path)  # cut.
            # вернуть адресс первого располоения:
            return False

        else:
            return None
