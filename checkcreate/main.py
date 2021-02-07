"""
    The module works only through import.
    Via os.system or return (RUN) - doesn't work.
"""

from delete.main import delete_file
from plugin import file_close, ErrorClearFile

if __name__ == "__main__":  # If not imported, I exit is the module:
    print("I am is Module!!! Bye Bye!!!")
    exit()  # Answer: I'm leaving, I'm a module.


def check_create_file(link):  # Check if the f is being created:
    """This module is required to create a f (or module)."""
    # Credo: Checking the f for editable...

    file_open = True  # A shortcut indicating that the file is open.
    f = None

    try:  # Create a file:
        f = open(link, 'x')
        return False

    except FileExistsError:  # The file was not created, so it is not open:
        file_open = False
        return True

    finally:
        if file_open:  # If the file open:
            file_close(f, "Я узнавал создам ли файл.")
        if delete_file(link) is None:  # Deleting a file:
            raise ErrorClearFile
