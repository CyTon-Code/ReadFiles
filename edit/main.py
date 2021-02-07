"""The module works only through import.
  Via os.system or return (RUN) - doesn't work."""
from check.main import check_file

error_code = 4


class FileDidNotClose(Exception):
    def __init__(self):
        print(f"error: {error_code}")


if __name__ == "__main__":  # If not imported, I exit is the module:
    print("I am is Module!!! Bye Bye!!!")
    exit()  # Answer: I'm leaving, I'm a module.
    pass


def check_file(link):  # Check if the file exists:
    """This module is required to read a file (or module).
    It can also check if a file (or module) exists."""
    # Credo: Checking file readability...
    if check_file(link):  # Я редактирую только если файл есть:
        pass
    file_open = True
    file = None

    try:  # create a file:
        file = open(link, 'w')
        return False  # Answer: The file is there.

    except:  # The file did not create but it is live:
        print("file is not created. file:", link)
        file_open = False  # At the end of the function, the file cannot be
        # closed (it has not been opened).

        return not file_open  # Answer: The file is missing or has not been read.

    finally:
        try:  # Closes the file:
            file.close()

        except:  # The file didn't close:
            if file_open:  # If the file open:
                raise FileDidNotClose  # Answer: The file won't close! We throw in
                # the program: "Exception".
