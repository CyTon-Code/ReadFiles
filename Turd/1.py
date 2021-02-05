def whats_file_name(path_file: str):  # "read/terminals/index.terminal"
    # Если это не ссылка а мусор то сваливаю:
    if path_file == "" or path_file == " " or path_file == "\n" or path_file == "\t":
        return None

    # Если это не ссилка, то это имя файла:
    if "/" not in path_file and "\\" not in path_file:
        return path_file

    # Возвращаю имя файла:
    name = ''
    for i in path_file:
        name += i
        if i in "\\/":
            name = ''

    return whats_file_name(name)


tmp = whats_file_name("read/terminals/index.terminal")
print(tmp, type(tmp))

tmp = whats_file_name("read/terminals/index.terminal/")
print(tmp, type(tmp))

tmp = whats_file_name("index.terminal")
print(tmp, type(tmp))

tmp = whats_file_name("")
print(tmp, type(tmp))
