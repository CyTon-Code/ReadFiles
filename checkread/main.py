"""The module works only through import.
  Via os.system or return (RUN) - doesn't work."""
from checkread import file_read, file_close

if __name__ == "__main__":  # If not imported, I exit is the module:
    print("I am is Module!!! Bye Bye!!!")
    exit()  # Answer: I'm leaving, I'm a module.
    pass


def check_read_file(link):  # Check if the file exists:
    """This module is required to read a file (or module).
    It can also check if a file (or module) exists."""
    # Credo: Checking file readability...

    file_open = True
    f = None

    try:  # Opens a file:
        f = open(link, 'r')
        return file_read(f)

    except:  # The file did not open:
        print("File is not defined. File:", link)
        file_open = False  # At the end of the function, the file cannot be
        # closed (it has not been opened).

        return not file_open  # Answer: The file is missing or has not been
        # read.

    finally:
        file_close(f, file_open)
