def odds_sum(data):
    if not isinstance(data, int) or data < 0:
        raise TypeError
    o_sum = 0
    for i in str(data):
        if int(i) % 2 != 0:
            o_sum += int(i)
    return o_sum
