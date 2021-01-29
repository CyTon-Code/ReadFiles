"""The module works only through import.
    Via os.system or return (RUN) - doesn't work."""


if __name__ == "__main__":  # If not imported, I exit is the module:
  print("I am is Module!!! Bye Bye!!!")    
  exit()  # Answer: I'm leaving, I'm a module.


def DeleteFile(AddressFile):  # Удаляем существующий файл.
  if CheckFile(AddressFile) != True:  # Если файл не существует:
    return False  # Файла для удаления не существует.
    # Если цель ваша просто удалить файл, то можете сменить на:
    #'return True'
  
  try:  # Удаляем файл: 
    #delete_file(AddressFile)
    return True  # Файл сущестовал и удалился.
  
  except:  # Удалить не получилось:
    return None  # Файл существует но не удалился.
