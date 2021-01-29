# Функция проверки файла (на редактирование и создание) перед работой с ним.
"""The module works only through import.
  Via os.system or return (RUN) - doesn't work."""


if __name__ == "__main__":  # If not imported, I exit is the module:
  print("I am is Module!!! Bye Bye!!!")    
  exit()  # Answer: I'm leaving, I'm a module.
  pass

def WriteFile(AddressFile):  # Check if the file exists:
  """This module is required to read a file (or module).
  It can also check if a file (or module) exists."""
  # Credo: ...
  
  FileOpen = True
  
  if CheckFile(AddressFile):  # Файла нет:
    # Я буду проверять на создание файла.
    try:  # Создаю файл:
      File = open(AddressFile, 'w')
      return False
    
    except:  # Файл не создался:
      print("File is not created. File:", AddressFile)
      return True

    finally:
      try:  # Закрываю файл:
        File.close()
        pass

      except:  # Файл не закрылся:
        raise Error
    
  else:  # файл есть:
    # Я буду проверять на редактирование файла.
    try:  # Открываю файл:
      File = open(AddressFile, 'w')

      try:  # записываю в файл:
        File.write('')
        return False

      except:  # Записать не получилось:
        return None

    except:  # Файл не открылся:
      print("File is not defined. File:", AddressFile)
      FileOpen = False

      return not FileOpen

    finally:
      try:  # Закрываю файл:
        File.close()
        pass

      except:  # Файл не закрылся:
        raise Error
    pass
  pass
