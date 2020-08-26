import pandas as pd
import matplotlib.pyplot as plt

df_item = pd.read_csv('../data/item-features.csv', index_col=None, header=0)
df_item.drop(['item_id'], axis=1, inplace=True)
df_item.columns = df_item.columns.astype(int)

print(df_item)

df_item[range(16)].hist(alpha=0.85, bins=20)
plt.show()
df_item[range(16, 32)].hist(alpha=0.85, bins=20)
plt.show()
