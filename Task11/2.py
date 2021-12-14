def remember_result(fn):
    last_result = None

    def wrapper(*args):
        nonlocal last_result
        print(f"Last result = '{str(last_result)}'")
        last_result = fn(*args)
    return wrapper


@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        result += str(item)
    print(f"Current result = '{result}'")
    return result
