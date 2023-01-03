def is_leaf(n):

    if n % 4 == 0:
        if n % 100 == 0 and n % 400 != 0:
            n = "平年"
        else:
            n = "闰年"
    else:
        n = "平年"
    return n