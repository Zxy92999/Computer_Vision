import random


def random_int(ranges=[0, 100], num=1):
    if ranges[0] > ranges[1]:
        print('取值范围错误')
        return []
    res = []
    for i in range(num):
        res.append(random.randint(ranges[0], ranges[1] + 1))
    return res


def random_float(ranges=[0, 100], num=1):
    if ranges[0] > ranges[1]:
        print('取值范围错误')
        return []
    res = []
    for i in range(num):
        res.append(random.random() * (ranges[1] - ranges[0]) + ranges[0])
    return res


