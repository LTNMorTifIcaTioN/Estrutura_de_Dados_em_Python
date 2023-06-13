import networkx as nx
import matplotlib.pyplot as plt

class visualizacaoGrafo:

    def __init__(self):
        self.visual = []

    def adicionaAresta(self, a, b):
        temp = [a,b] # armazena a aresta temporária
        self.visual.append(temp) # insere na lista visual

    def desenhar(self):
        G = nx.Graph() # cria-se um grafo G
        # adiciona-se então a lista de arestas a G
        G.add_edges_from(self.visual)
        # executa-se a função de desenho
        nx.draw_networkx(G, node_color='lightgrey')
        # o grado é então desenhado na tela
        plt.show()

G = visualizacaoGrafo()
G.adicionaAresta('Pedro', 'CP')
G.adicionaAresta('Pedro', 'Carla')
G.adicionaAresta('Carla', 'CP')
G.adicionaAresta('Pedro', 'CC')
G.adicionaAresta('João', 'CC')
G.desenhar()
