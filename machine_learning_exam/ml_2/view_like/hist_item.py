import pandas as pd
import matplotlib.pyplot as plt

df_train = pd.read_csv('../data/train.csv', index_col=None)

df_item = df_train.groupby('item_id').size()
df_like_item = df_train[df_train['like'] == 1].groupby('item_id').size()

item_id = sorted(df_item.index.tolist())
item_id_like = sorted(df_like_item.index.tolist())
all_item_id = [i for i in range(444)]

item_id_not_like = sorted(set(all_item_id) - set(item_id_like))
item_id_not = sorted(set(all_item_id) - set(item_id))

print(f'Количество баннеров с лайками: {len(item_id_like)}')
print(f'Количество баннеров без лайков: {len(item_id_not_like)}')
print(f'Количество баннеров, которые ни разу не лайкнули и не дизлайкнули: {len(item_id_not)}')

plt.hist(df_item, bins=25)
plt.show()

plt.hist(df_like_item, bins=50)
plt.show()
