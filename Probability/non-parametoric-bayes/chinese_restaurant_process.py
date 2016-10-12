# coding:utf-8
"""
中華料理屋過程シミュレーション
"""

import numpy as np
import matplotlib.pyplot as plt

N = 1000  # 客数
alpha = 1  # 集中度
table = []  # テーブル

cluster_num = []
table.append(1)

for n in range(2, N):

    p = np.array(table + [alpha]) / (n - 1 + alpha)
    c = np.random.choice(range(len(table) + 1), p=p)

    if len(table) == c:
        table.append(1)
    else:
        table[c] += 1
    cluster_num.append(len(table))

print(table)
plt.plot(cluster_num)
plt.show()
