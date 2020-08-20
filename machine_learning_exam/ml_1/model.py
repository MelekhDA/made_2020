import pandas as pd

from sklearn.svm import SVC

fields = [0, 2, 5, 6, 8, 10, 12, 13, 14, 19, 28, 29]

train_x = pd.read_csv('data/train.csv', header=None)
train_y = pd.read_csv('data/train-target.csv', header=None)
test_x = pd.read_csv('data/test.csv', header=None)

train_x = train_x[fields].copy()
train_y = train_y[0]
test_x = test_x[fields]

svm = SVC(probability=True, C=40)

svm.fit(train_x, train_y)

y_predict_val = svm.predict_proba(test_x)

df = pd.DataFrame()
df[0] = y_predict_val[:, 1].T

print(df)
# df.to_csv('test_predict_proba_v5.3.csv', index=False, header=False)
