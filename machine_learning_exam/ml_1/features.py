import pandas as pd
import math
import matplotlib.pyplot as plt

N = 30
header_x = [i for i in range(N)]

train_x = pd.read_csv('data/train.csv', header=None)
test_x = pd.read_csv('data/test.csv', header=None)

train_x_corr = train_x.corr()
test_x_corr = test_x.corr()

results = {}

for i in header_x:
    arr = []
    for j in header_x:
        tr = train_x_corr[i][j]
        ts = test_x_corr[i][j]

        if math.fabs(tr - ts) > 0.5 * math.fabs(tr):
            arr.append(j)

    results[i] = arr

for i, v in sorted(results.items(), key=lambda x: len(x[1])):
    print(i, len(v), v)

plt.plot(range(len(results)), [len(v) for _, v in sorted(results.items(), key=lambda x: len(x[1]))])
plt.show()
