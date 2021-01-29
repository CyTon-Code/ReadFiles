"""The module works only through import.
    Via os.system or return (RUN) - doesn't work."""


if __name__ == "__main__":  # If not imported, I exit is the module:
  print("I am is Module!!! Bye Bye!!!")    
  exit()  # Answer: I'm leaving, I'm a module.
  pass


import os


def DeleteFile(AddressFile):  # Delete existing file:
  if CheckFile(AddressFile):  # If the file does not exist:
    return False  # Answer: The file to be deleted does not exist.

  try:  # Delete the file:
    os.remove(AddressFile)
    return True  # Answer: The file existed and was deleted.

  except:  # Delete failed:
    return None  # Answer: The file exists but has not been deleted.
