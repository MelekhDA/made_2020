BIG_NUMBER = 35184372089371


def get_number(k):
    start = [1, 1]
    index_1 = -1
    n = len(start)

    for _ in range(1, k):
        if start[0] == 1 and start[1] == 1:
            start = [1] + [0 for _ in range(n - 1)] + [1]
            index_1 = -1
            n += 1
        else:
            start[index_1], start[index_1 - 1] = 0, 1
            index_1 -= 1

    return int(''.join(map(str, start)), 2)


for _ in range(int(input())):
    result = get_number(int(input()))

    if result > BIG_NUMBER:
        result %= BIG_NUMBER
    elif result == BIG_NUMBER:
        result = 0

    print(result)
