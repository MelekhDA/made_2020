import pandas as pd
import matplotlib.pyplot as plt

df_item = pd.read_csv('../data/item-features.csv', index_col=None, header=0)

column, n = '0', 20

item_1 = df_item[column]
mean = item_1.mean()
median = item_1.median()
std = item_1.std()

list_data = [(int(row['item_id']), row[column], abs(row[column] - median) / (std)) for _, row in
             df_item.iterrows()]
list_data = sorted(list_data, key=lambda x: x[2], reverse=True)

item_id_noise, list_dist = [], []
for item_id, _, dist in list_data[:n]:
    item_id_noise.append(item_id)
    list_dist.append(dist)

x_points = [i for i, _ in enumerate(item_id_noise)]

plt.plot(x_points, list_dist, 'bo', markersize=4, linewidth=1, linestyle='-', alpha=0.8)
plt.yticks(range(10))
plt.xticks(x_points, item_id_noise)
plt.xlabel('Id баннера')
plt.grid()
plt.show()
