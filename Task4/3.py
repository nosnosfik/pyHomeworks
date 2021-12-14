def my_split(data, delimiter):
    word = ''
    new_list = []
    if not isinstance(data, str):
        raise ValueError
    for char in data:
        if char == delimiter:
            new_list.append(word)
            word = ''
            continue
        word += char
    new_list.append(word)
    return new_list