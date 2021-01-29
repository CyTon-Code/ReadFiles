# If not imported, I exit is the module:
if __name__ == "__main__":
    print("I am is Module!!! Bye Bye!!!")    
    exit()
    pass


def CheckFile(AddressFile):  # Check if the file exists:
    # credo: Checking file readability...
    """This module is required to read a file (or module).
    It can also check if a file (or module) exists."""
    
    try:  # Opens a file:
        File = open(AddressFile, 'r')
        
        try:  # The file is read:
            File.read()
            return True  # answer: The file is there, and it has been read.
        
        except:  # File not read:
            pass  # answer: The file is present, but not readable.
    
    except:  # The file did not open:
        print("File is not defined. File:", AddressFile)
        return False  # answer: The file is missing or has not been read.
    
    finally:
        try:  # Closes the file:
            File.close()
        
        except:  # The file didn't close:
            #  ~ raise Exception
            pass  # answer: The file won't close! We throw in the program: "Exception".
    pass
