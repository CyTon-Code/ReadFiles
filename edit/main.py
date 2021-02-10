"""
    The module works only through import.
    Via os.system or return (RUN) - doesn't work.
"""

from checkopen.main import check_file
from plugin import file_close

if __name__ == "__main__":  # If not imported, I exit is the module:
    print("I am is Module!!! Bye Bye!!!")
    exit()  # Answer: I'm leaving, I'm a module.


def edit_file(link: str, line_of_text="") -> bool or Exception:  # Edit file if it exists:
    """
        This module is required to read a file (or module).
        It can also check if a file (or module) exists.
    """  # Credo: Checking file readability...

    if check_file(link):  # I only edit if the file exists:
        return None

    file_open = True
    file = None

    try:  # modify file:
        file = open(link, 'w')
        
        # editing a file:
        file.write(line_of_text)
        return True  # Answer: The file has been edited.
    
    except:  # The file has not been modified, but it exists:
        # Failed to modify file:
        print("the file has not changed. file:", link)
        file_open = False  # At the end of the function, the file cannot be
        # closed (it has not been opened).
        # Answer: The file was not edited.
        return False  # Answer: The file is missing or has not been read.

    finally:
        if file_open:  # If the file open:
            file_close(file, "Я пытался редактировать файл")
