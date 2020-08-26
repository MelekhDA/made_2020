import pandas as pd
import matplotlib.pyplot as plt

df_item = pd.read_csv('../data/item-features.csv', index_col=None, header=0)
df_item.drop(['item_id'], axis=1, inplace=True)
df_item.columns = df_item.columns.astype(int)

columns = df_item.columns[:4].tolist()

df_item.boxplot(column=columns)
plt.show()

for col in columns:
    plt.hist(df_item[col], alpha=0.85, bins=150)
    plt.show()
