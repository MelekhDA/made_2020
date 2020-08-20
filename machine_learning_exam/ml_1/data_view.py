import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def hist_by_class(train):
    fields, n_bins = [9, 15, 16, 26], 30

    fig, axes = plt.subplots(nrows=2, ncols=2)
    ax_s = axes.flatten()

    for field, ax in zip(fields, ax_s):
        ax.hist(train[train.target == 0][field], n_bins, alpha=0.7)
        ax.hist(train[train.target == 1][field], n_bins, alpha=0.7)
        ax.set_title(f'field_{field}')

    fig.tight_layout()
    plt.show()


train_x = pd.read_csv('data/train.csv', header=None)
train_y = pd.read_csv('data/train-target.csv', header=None)
test_x = pd.read_csv('data/test.csv', header=None)

train = train_x.copy()
train['target'] = train_y[0].copy()

print(pd.concat([train_x.head(10), train_x.tail(10)]))

print(train_x.describe().to_string())

for df in [train_x, test_x]:
    sns.heatmap(df.corr(), annot=True, cbar=False)
    plt.show()

train_x[range(16)].hist(alpha=0.85, bins=20)
plt.show()
train_x[range(16, 30)].hist(alpha=0.85, bins=20)
plt.show()

test_x[range(16)].hist(alpha=0.85, bins=20)
plt.show()
test_x[range(16, 30)].hist(alpha=0.85, bins=20)
plt.show()

hist_by_class(train)
