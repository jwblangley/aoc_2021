def get_num_increased(it):
    res = 0
    prev = next(it)

    for curr in it:
        if curr > prev:
            res += 1
        prev = curr

    return res
