def multiplication_table():
    s = ''
    for i in range(1, 10):
        for j in range(1, i+1):
            s += '{} * {} = {}'.format(i, j, i*j) + "\t"
        s += "\n"
    return s