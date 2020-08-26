import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_item = pd.read_csv('../data/item-features.csv', index_col=None, header=0)

drop_items = [441, 284, 285, 291, 424, 287, 286, 425, 289, 292, 383, 384]

df_item = df_item[~df_item['item_id'].isin(drop_items)]

df_item.drop(['item_id'], axis=1, inplace=True)
df_item.columns = df_item.columns.astype(int)

sns.heatmap(df_item.corr(), annot=True, cbar=False)
plt.show()
