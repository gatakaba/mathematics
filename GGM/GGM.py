# coding:utf-8
# Graphical Gaussian Model習作


import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

N = 1000

x1 = np.sin(np.linspace(0, 2 * np.pi, N)) + np.random.normal(size=N)
x2 = np.cos(np.linspace(0, 2 * np.pi, N)) + np.random.normal(size=N)
x3 = x1 + x2 + np.random.normal(size=N)
x4 = np.tan(np.linspace(0, 2 * np.pi, N)) + np.random.normal(size=N)
x5 = np.cumsum(np.random.normal(size=N)) + np.random.normal(size=N)
x6 = np.cumsum(np.random.normal(size=N)) + np.random.normal(size=N)

X = np.r_[x1, x2, x3, x4, x5, x6]

X = np.c_[x1, x2, x3, x4, x5, x6]
X = (X - np.mean(X, axis=0)) / np.std(X, axis=0)

Ad = np.cov(X.T)

# 閾値以下の相関の場合グラフカット(本当はやってはいけない)
Ad[np.where(np.abs(Ad) < 0.2)] = 0
Ad[np.diag_indices(len(Ad))] = 0

Ad = np.round(Ad, 2)

graph = nx.from_numpy_matrix(Ad)

print(Ad)
# pos = nx.circular_layout(graph)
# pos = nx.shell_layout(graph)
# pos = nx.random_layout(graph)
# pos = nx.spectral_layout(graph)
pos = nx.spring_layout(graph)
# pos = nx.circular_layout(grap
# h)
nx.draw_networkx_nodes(graph, pos, node_size=300, node_color="w")
nx.draw_networkx_edges(graph, pos, width=1)

nx.draw_networkx_labels(graph, pos, font_size=16, font_color="r")
nx.draw_networkx_edge_labels(graph, pos)

plt.xticks([])
plt.yticks([])
plt.show()
