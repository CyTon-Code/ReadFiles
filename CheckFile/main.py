"""The module works only through import.
  Via os.system or return (RUN) - doesn't work."""


if __name__ == "__main__":  # If not imported, I exit is the module:
  print("I am is Module!!! Bye Bye!!!")    
  exit()  # Answer: I'm leaving, I'm a module.


def CheckFile(AddressFile):  # Check if the file exists:
  """This module is required to read a file (or module).
  It can also check if a file (or module) exists."""
  # Credo: Checking file readability...
  Process = False

  try:  # Opens a file:
    File = open(AddressFile, 'r')

    try:  # The file is read:
      File.read()
      Process = True  # Answer: The file is there, and it has been read.
        
    except:  # File not read:
      Process = None  # Answer: The file is present, but not readable.
    
  except:  # The file did not open:
    print("File is not defined. File:", AddressFile)
    Process = False  # Answer: The file is missing or has not been read.
    
  finally:
    try:  # Closes the file:
      File.close()

    except:  # The file didn't close:
      if (Process != False):
        raise Exception  # Answer: The file won't close! We throw in the program: "Exception".
    
    return Process
  pass
