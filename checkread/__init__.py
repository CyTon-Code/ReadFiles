error_code = "Я пытался открывать и читать файл."


class FileDidNotClose(Exception):
    def __init__(self):
        print(f"error: {error_code}")


def check_read(file):
    try:  # The file is read:
        file.read()
        return False  # Answer: The file is there, and it has been read.

    except:  # file not read:
        return None  # Answer: The file is present, but not readable.
