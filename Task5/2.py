import math


def arithm_progression_product(a1, t, n):
    arr = [a1]
    for i in range(n - 1):
        arr.append(arr[i] + t)
    return math.prod(arr)