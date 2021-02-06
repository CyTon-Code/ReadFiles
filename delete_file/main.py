"""The module works only through import.
  Via os.system or return (RUN) - doesn't work."""

if __name__ == "__main__":  # If not imported, I exit is the module:
    print("I am is Module!!! Bye Bye!!!")
    exit()  # Answer: I'm leaving, I'm a module.
    pass

from check_file.main import check_file
import os


def delete_file(address_file):  # Delete existing file:
    if check_file(address_file):  # If the file does not exist:
        return False  # Answer: The file to be deleted does not exist.

    try:  # Delete the file:
        os.remove(address_file)
        return True  # Answer: The file existed and was deleted.

    except:  # Delete failed:
        return None  # Answer: The file exists but has not been deleted.
# FileNotFoundError TypeError OSError IsADirectoryError:
