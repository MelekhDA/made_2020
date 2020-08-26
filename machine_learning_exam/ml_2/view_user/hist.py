import pandas as pd
import matplotlib as mpl

mpl.rcParams['xtick.labelsize'] = 6

df_user = pd.read_csv('../data/user-features.csv', index_col=None, header=0)
df_user.drop(['user_id'], axis=1, inplace=True)
df_user.columns = df_user.columns.astype(int)

print(df_user)

df_user[range(16)].hist(alpha=0.85, bins=10)
mpl.pyplot.show()
df_user[range(16, 32)].hist(alpha=0.85, bins=10)
mpl.pyplot.show()
