def call_once(fn):
    cache = None
    def wrapper(*args):
        nonlocal cache
        if not cache:
            cache = fn(*args)
        return cache
    return wrapper


@call_once
def sum_of_numbers(a, b):
    return a + b
