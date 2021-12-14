def sum_geometric_elements(a: float, t: float, lim: float) -> float:
    if not 0 < t < 1:
        raise ValueError
    if not a > 0 or not lim > 0:
        raise ValueError
    arr = [a]
    while True:
        if a * t < lim:
            break
        arr.append(a * t)
        a *= t
    print(arr)
    return round(math.fsum(arr), 3)