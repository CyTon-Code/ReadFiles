"""The module works only through import.
  Via os.system or return (RUN) - doesn't work."""


class TheFileDidNotClose(Exception):
    pass


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

        try:  # The file is read:
            f.read()
            return False  # Answer: The file is there, and it has been read.

        except:  # f not read:
            return None  # Answer: The file is present, but not readable.

    except:  # The file did not open:
        print("File is not defined. File:", link)
        file_open = False  # At the end of the function, the file cannot be
        # closed (it has not been opened).

        return not file_open  # Answer: The file is missing or has not been
        # read.

    finally:
        try:  # Closes the file:
            f.close()

        except:  # The file didn't close:
            if file_open:  # If the file open:
                raise TheFileDidNotClose  # Answer: The file won't close! We
                # throw in the program: "Exception".
