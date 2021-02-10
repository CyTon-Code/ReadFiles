"""
    The module works only through import.
    Via os.system or return (RUN) - doesn't work.
"""

import os
from checkopen.main import check_file
from whatsfilename.main import whats_file_name

if __name__ == "__main__":  # If not imported, I exit is the module:
    print("I am is Module!!! Bye Bye!!!")
    exit()  # Answer: I'm leaving, I'm a module.


def moving_a_file(link: str, path="work/moving_a_file.py"):
    # If the names are the same, but the addresses are different, you can move:
    if link == path or not whats_file_name(link) == whats_file_name(path):
        return True
    
    else:  # Перемещаем и переменовываем файл:
        if check_file(link):  # if (os.path.exists(link)):
            os.replace(link, path)  # cut
            return False

        else:  # There is no file, so there is no point in moving:
            return None
