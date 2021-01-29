if __name__ == "__main__":
    print("I am is Module!!!")
    print("Bye Bye!!!")
    # If not imported, i exit is the module.
    exit()

# проверить есть ли файл:
def check_file(address_file):  #echo Checking module readability...
    # Module Нужен для чтения файла и проверки на сущестование файла или модуля.
    
    try:
        f = open(address_file, 'r') # если ошибка, то: файла нет или
        # его нельзя читать.
        return True # ответ: файл есть и его прочитано.
    except:
        print("Module not defined. modul:", address_file)
        return False # ответ: файла нет или его не прочитано.
    finally:
        try:
            f.close() # обьязательно нужно закрыть файл, если еще не
            # закрылся (функция сама это сделает).
        except:
            pass # return None # я считаю сюда попасть - еденичный случай
            # И если попасть в это место, то файл нельзя закрыть читая: файл
            # нельзя закрыть или изчез, возможно этот сбой - еденичный случай.
