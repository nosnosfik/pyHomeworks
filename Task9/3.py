import re

def get_longest_word(s: str) -> str:
    if type(s) is not str:
        raise ValueError
    for sym in s:
        if not (sym.isalpha() or sym.isspace() or sym.isdecimal()):
            s = s.replace(sym, '')
    return sorted(re.split(r'\W', s), key=lambda x: len(x), reverse=True)[0]