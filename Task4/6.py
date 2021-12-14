def get_longest_word(data):
    if not isinstance(data, str):
        raise ValueError
    return max(data.split(), key=len)