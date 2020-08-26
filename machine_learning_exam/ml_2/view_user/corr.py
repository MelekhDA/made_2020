import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_user = pd.read_csv('../data/user-features.csv', index_col=None, header=0)
df_user.drop(['user_id'], axis=1, inplace=True)

sns.heatmap(df_user.corr(), annot=True, cbar=False)
plt.show()
