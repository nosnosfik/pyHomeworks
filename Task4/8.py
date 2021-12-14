def get_pairs(data):
    final_list = []
    for i, v in enumerate(data):
        if i < len(data) - 1:
            final_list.append((v, data[i + 1]))
        elif len(data) < 2:
            return None
    return final_list