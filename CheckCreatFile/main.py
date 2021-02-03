def CheckCreatFile(AddressFile):  # Check if the file is being created:
  """This module is required to create a file (or module)."""
  # Сredo: Checking the file for editable...
  
  if CheckFile:  # Если файл существует:
    return False
  
  FileOpen = True
  
  try:  # Создаю файл:
    File = open(AddressFile, 'w')
    return True
  
  except:  # Файл не создался:
    return None
    FileOpen = False
  
  finally:  # Завершаю 
    try:  # Закрываю файл:
      File.close()
      
      try:
        # TODO DeleteFile(AddressFile)
        pass
      
      except:
        # raise ErrorClearFile
        pass

    except:  # Файл не закрылся:
      if FileOpen:  # If the file open:
        raise ErrorExitFile
