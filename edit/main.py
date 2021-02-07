"""
    The module works only through import.
    Via os.system or return (RUN) - doesn't work.
"""

from check.main import check_file
from plugin import file_close

if __name__ == "__main__":  # If not imported, I exit is the module:
    print("I am is Module!!! Bye Bye!!!")
    exit()  # Answer: I'm leaving, I'm a module.
    pass


def edit_file(link):  # Edit file if it exists:
    """This module is required to read a file (or module).
    It can also check if a file (or module) exists."""
    # Credo: Checking file readability...
    if check_file(link):  # I only edit if the file exists:
        pass

    file_open = True
    f = None

    try:  # create a file:
        f = open(link, 'w')
        return False  # Answer: The file is there.

    except:  # The file did not create but it is live:
        print("file is not created. file:", link)
        file_open = False  # At the end of the function, the file cannot be
        # closed (it has not been opened).

        return not file_open  # Answer: The file is missing or has not been read.

    finally:
        if file_open:  # If the file open:
            file_close(f, "Я пытался редактировать файл")
