def split_by_index(data, indexes):
    start_slice = 0
    new_list = []
    for index in indexes:
        if not isinstance(index, int) or index <= start_slice:
            continue
        new_list.append(data[start_slice:index])
        start_slice = index
    if start_slice < len(data):
        new_list.append(data[start_slice:])
    return new_list