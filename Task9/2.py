def is_palindrome(test_string: str) -> bool:
    if type(test_string) is not str:
        raise ValueError
    test_string = test_string.lower()
    for sym in test_string:
        if not sym.isalpha():
            test_string = test_string.replace(sym, '')
    return test_string == "".join(reversed(test_string))