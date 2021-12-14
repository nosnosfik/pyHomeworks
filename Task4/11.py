def fibonacci_loop(seq):
    final_string = ''
    for i in seq:
        if isinstance(i, int):
            final_string += f'{i} '
        elif isinstance(i, float):
            continue
        elif isinstance(i, str):
            break
    return final_string.rstrip()