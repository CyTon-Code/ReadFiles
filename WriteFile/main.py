# Функция проверки файла (на редактирование и создание) перед работой с ним.
"""The module works only through import.
  Via os.system or return (RUN) - doesn't work."""


if __name__ == "__main__":  # If not imported, I exit is the module:
  print("I am is Module!!! Bye Bye!!!")    
  exit()  # Answer: I'm leaving, I'm a module.
  pass


def CreatFile(AddressFile):
  f = open(AddressFile, 'w')
  f.close()
  pass


def 


def WriteFile(AddressFile):  # Check if the file exists:
  """This module is required to read a file (or module).
  It can also check if a file (or module) exists."""
  # Сredo: Checking the file for editable...
  
  FileOpen = True
  try:  # Открываю файл или Создаю файл:
    File = open(AddressFile, 'w')

    if CheckFile(AddressFile):  # Если файла нет:
      # Я буду проверять на создание файла:
      try: Создаю файл:
        f = open(AddressFile, 'w')
        f.close()
        return False
      
      except: Не создал файл:
        FileOPn = False
        return None

      #     except:
      #       pass
      finally:
        try: Удаляю файл
          from DeleteFile import main.DeleteFile
          main.DeleteFile(AddressFile)

        except: Не удалил файл:
          if FileOpen:  # If the file open:
            raise ErrorCreat
        
      #TODO Нужно удалить за собой файл AddressFile
      FileOpen = False  # Нужно сказать что файл не открылся.
      return False  # Файл создать можно.

    else:  # Файл есть:
      # Я буду проверять на редактирование файла:
      try:  # записываю в файл:
        File.write('')
        return False

      except:  # Записать не получилось:
        return None

  except:  # Файл не открылся или не создался:
    print("File is not defined. File:", AddressFile)
    FileOpen = False

    return not FileOpen  # True

  finally:
    try:  # Закрываю файл:
      File.close()
      pass

    except:  # Файл не закрылся:
      if FileOpen:  # If the file open:
        raise ErrorEdit
  pass
