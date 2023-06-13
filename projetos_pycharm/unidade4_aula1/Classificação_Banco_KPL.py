import matplotlib.pyplot as plt
import networkx as nx

edges = [['Loja 1', 'Cliente'], ['Cliente', 'Loja 2'], ['Cliente', 'Loja 3']]
G = nx.Graph()
G.add_edges_from(edges)
pos = nx.spring_layout(G)
plt.figure()
nx.draw(G, pos, edge_color='black', width=1, linewidths=1,\
node_size=1500, node_color='lightgrey', alpha=0.9,\
labels={node:node for node in G.nodes()})
nx.draw_networkx_edge_labels(G, pos, edge_labels={('Loja 1', 'Cliente'):'Transações - 2', \
('Cliente', 'Loja 2'):'Transações - 15', ('Cliente', 'Loja 3'):'Transações - 7'}, font_color='red')
plt.axis('off')
plt.show()
