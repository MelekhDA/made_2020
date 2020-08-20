from math import factorial as f, gcd


def c(n, k):
    return f(n) // (f(n - k) * f(k))


for _ in range(int(input())):
    k = int(input())

    result = 0

    for i in range(k):
        arr = map(int, input().split())
        result += sum(v * c(i, j) * 2 ** (k - i - 1) for j, v in enumerate(arr))

    result = int(result)
    delimiter = int(2 ** (k - 1))

    all_del = gcd(result, delimiter)
    result, delimiter = result // all_del, delimiter // all_del

    if result == 0:
        print(1, 0)
    else:
        print(result, delimiter)
