import pandas as pd
import matplotlib.pyplot as plt

df_item = pd.read_csv('../data/item-features.csv', index_col=None, header=0)

drop_index = [424, 441, 285, 286, 287, 289, 425, 383, 384, 291, 284, 292]  # 384

results = {i: [] for i in df_item['item_id']}

for column in df_item.columns[1:]:
    item_1 = df_item[column]
    mean = item_1.mean()
    median = item_1.median()
    std = item_1.std()

    list_data = [(int(row['item_id']), row[column], abs(abs(row[column]) - abs(median)) / std) for _, row in
                 df_item.iterrows()]
    list_data = sorted(list_data, key=lambda x: x[2], reverse=True)

    for obj in list_data:
        item_id, _, val = obj
        results[item_id].append(val)

for k, v in results.items():
    results[k] = sum(v) / len(v)

item_id_noise, list_dist = [], []
for item_id, val in sorted(results.items(), key=lambda x: x[1], reverse=True):
    item_id_noise.append(item_id)
    list_dist.append(val)

n = 20
x_points = [i for i, _ in enumerate(item_id_noise)]

print(item_id_noise[:n])

plt.plot(x_points[:n], list_dist[:n], 'bo', markersize=4, linewidth=1, linestyle='-', alpha=0.8)
plt.yticks(range(10))
plt.xticks(x_points[:n], item_id_noise[:n])
plt.xlabel('Id баннера')
plt.grid()
plt.show()
