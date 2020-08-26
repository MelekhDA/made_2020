import pandas as pd
import matplotlib.pyplot as plt

df_train = pd.read_csv('../data/train.csv', index_col=None)

print(df_train)

df_like_item = df_train[df_train['like'] == 1].groupby('item_id').size()
df_dislike_item = df_train[df_train['like'] == 0].groupby('item_id').size()

df_like_true = pd.DataFrame()
df_like_true['item_id'] = df_like_item.index
df_like_true['rating'] = df_like_item - df_dislike_item
df_like_true = df_like_true.sort_values('rating', ascending=False)

n = 50

df_like_true = df_like_true.head(n)

x_points = [i for i, _ in enumerate(df_like_true['item_id'])][:n]

plt.plot(x_points, df_like_true['rating'], 'bo', markersize=2, linewidth=1, linestyle='-', alpha=0.8)
plt.xticks(x_points, df_like_true['item_id'], fontsize=8, rotation=90)
plt.xlabel('Id баннера')
plt.ylabel('Разница между количеством лайков и дизлайков')
plt.grid()
plt.show()
