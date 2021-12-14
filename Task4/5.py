def get_digits(*args):
    args = args
    new_list = []
    for i in args:
        for y in str(i):
            new_list.append(int(y))
    return tuple(new_list)