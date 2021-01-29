"""The module works only through import.
    Via os.system or return (RUN) - doesn't work."""


if __name__ == "__main__":  # If not imported, I exit is the module:
  print("I am is Module!!! Bye Bye!!!")    
  exit()  # Answer: I'm leaving, I'm a module.
  pass


#Удалить файл
def delete_file():
    """
    https://github.com/khomaldi/pyconsoleeditor/blob/065f66637d1ec8bcfa530307d43611d823dd1110/py.py#L170
    """
    name = input('Введине имя файла: ')
    os.remove(name)
    clear()
    menu_programm()
    pass


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
