from math import factorial

for i in range(int(input())):
    arr = {}

    for j in range(int(input())):
        x, y = map(int, input().split(' '))

        if x in arr.keys():
            arr[x].append(y)
        else:
            arr[x] = [y]

    x_s = list(arr.keys())
    res = 0

    for i, x1 in enumerate(x_s):
        for x2 in x_s[i + 1:]:
            confluence = list(set(arr[x1]) & set(arr[x2]))
            n = len(confluence)
            if n < 2:
                continue
            else:
                res += factorial(n) / (2 * factorial(n - 2))

    print(int(res))
