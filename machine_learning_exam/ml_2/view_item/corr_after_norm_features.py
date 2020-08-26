import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_item = pd.read_csv('../data/item-features-proccessing.csv', index_col=None, header=0)

df_item.drop(['item_id'], axis=1, inplace=True)
df_item.columns = df_item.columns.astype(int)

plt.figure(figsize=(10, 8))
sns.heatmap(df_item.corr().round(1), annot=True, cbar=False)
plt.savefig('features_corr_after_norm_features.png')
