def whats_file_name(link: str):
    # Expected example:  # "read/terminals/index.terminal"

    # If this is not a link, but garbage, then exit:
    if link == "" or link == " " or link == "\n" or link == "\t":
        return None

    # If it is not a link, then this is the filename:
    if "/" not in link and "\\" not in link:
        return link

    # Cut filename from link:
    name = ''
    for i in link:
        name += i
        if i in "\\/":
            name = ''

    # Return filename:
    return whats_file_name(name)


# test:
tmp = whats_file_name("read/terminals/index.terminal")
print(tmp, type(tmp))
