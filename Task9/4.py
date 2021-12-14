import string


def test_data(data):
    if not all(type(el) is str for el in data):
        raise TypeError


def chars_in_all(*strings):
    test_data(strings)

    if len(strings) < 2:
        return set()

    return set(strings[0]).intersection(*[set(el) for el in strings[1:]])


def chars_in_one(*strings):
    test_data(strings)

    if len(strings) < 2:
        return set(strings[0])

    return set(strings[0]).union(*[set(el) for el in strings[1:]])


def chars_in_two(*strings):
    if len(strings) < 2:
        raise ValueError

    test_data(strings)
    all_s = ''.join(strings)

    for letter in set(all_s):
        all_s = all_s.replace(letter, '', 1)

    return set(all_s)


def not_used_chars(*strings):
    return set(string.ascii_lowercase).difference(set(''.join(strings)))