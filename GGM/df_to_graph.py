import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

r = np.random.RandomState(seed=5)
ints = r.random_integers(1, 10, size=(3, 2))
a = ['A', 'B', 'C']
b = ['D', 'A', 'E']
df = pd.DataFrame(ints, columns=['weight', 'cost'])
df["source"] = a
df['target'] = b

# graph = nx.from_pandas_dataframe(df, "source", 'target', ['weight', 'cost'])
graph = nx.from_pandas_dataframe(df, "source", 'target', 'weight')

pos = nx.spring_layout(graph)

nx.draw_networkx_nodes(graph, pos, node_size=300, node_color="w")
nx.draw_networkx_edges(graph, pos, width=1)

nx.draw_networkx_labels(graph, pos, font_size=16, font_color="r")

nx.draw_networkx_edge_labels(graph, pos)
plt.xticks([])
plt.yticks([])
plt.show()
