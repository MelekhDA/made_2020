import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_item = pd.read_csv('../data/item-features.csv', index_col=None, header=0)
df_item.drop(['item_id'], axis=1, inplace=True)
df_item.columns = df_item.columns.astype(int)

sns.heatmap(df_item.corr())
plt.show()
