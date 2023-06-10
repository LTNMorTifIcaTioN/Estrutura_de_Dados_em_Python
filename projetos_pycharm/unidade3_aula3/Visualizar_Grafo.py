"""
Em caso de precisar visualizar um grafo, como ao colocar em alguma apresentação,
você pode usar a biblioteca networkx que é uma biblioteca Python que não faz parte da biblioteca padrão.
Para usá-la você tem que instalar com “pip install networkx”.
Ela usa a biblioteca matplolib que desenha gráficos. Com isso, você criar e pode visualizar seus grafos.
O código abaixo foi extraído do tutorial https://bit.ly/3x3WBEE
"""

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
E = [('A', 'B', 2), ('A', 'C', 1), ('B', 'E', 3), ('C', 'E', 2)]

G.add_weighted_edges_from(E)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold')
edge_weight = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_weight)
plt.show()