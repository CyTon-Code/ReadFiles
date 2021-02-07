from typing import IO

error_code = "Я пытался открывать и читать файл."


class FileDidNotClose(Exception):
    def __init__(self):
        print(f"error: {error_code}")


def file_read(file):
    try:  # The file is read:
        file.read()
        return False  # Answer: The file is there, and it has been read.

    except:  # file not read:
        return None  # Answer: The file is present, but not readable.


def file_close(file: IO, file_open: bool):
    try:  # Closes the file:
        file.close()

    except:  # The file didn't close:
        if file_open:  # If the file open:
            raise FileDidNotClose  # Answer: The file won't close! We
            # throw in the program: "Exception".
