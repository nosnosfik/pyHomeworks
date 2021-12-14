def swap_quotes(string):
    new_string = []
    for char in string:
        if char == '"':
            new_string.append("'")
        elif char == "'":
            new_string.append('"')
        else:
            new_string.append(char)
    return ''.join(new_string)
