def paly(data):
    if not data.isalpha():
        raise ValueError
    tmp = ""
    data = data.lower()
    for char in data:
        tmp = char + tmp
    return data == tmp