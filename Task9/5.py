def count_letters(s: str) -> dict:
    if type(s) is not str:
        raise TypeError
    tmp_dict = {}
    for sym in set(s):
        if sym.isalpha():
            tmp_dict[sym] = s.count(sym)
    return tmp_dict
