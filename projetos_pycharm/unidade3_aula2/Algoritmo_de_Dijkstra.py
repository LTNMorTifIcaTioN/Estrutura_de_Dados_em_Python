"""
Algoritmo de Dijkstra
"""
class Grafo:
    def __init__(self, orientado=False):
        # dict em que as chaves são os nomes de vértices origem
        # e os valores são os pares de vértices destino e custo
        self._lista_de_adjacencias = dict()
        self.orientado = orientado


    @property
    def vertices(self):
        """Retorna os nomes dos vértices"""
        return set(self._lista_de_adjacencias.keys())

    def arestas(self, v_origem=None):
        """Retorna as arestas do vértice 'v_origem' ou do grafo inteiro"""
        if v_origem:
            # obtém arestas do vértice
            return self.v_arestas(v_origem)

        # retorna arestas do grafo inteiro
        arestas_do_grafo = []
        for v_origem in self.vertices:
            # acumula as arestas de todos os vértices
            arestas_do_grafo += self.v_arestas(v_origem)
        return arestas_do_grafo

    def v_arestas(self, v_origem):
        """Retorna as arestas do vértice 'v_origem' """
        # retorna arestas de um vértice
        arestas = []
        for v_destino, custo in self._lista_de_adjacencias[v_origem]:
            arestas.append((v_origem, v_destino, custo))
        return arestas

    def inserir_aresta(self, u, v, custo):
        """Cria uma aresta entre os vértices 'u' e 'v'"""

        # cria uma chave 'u' com valor lista vazia no dicionário,
        # se chave 'u' não existir
        self._lista_de_adjacencias.setdefault(u, [])

        # cria uma chave 'v' com valor lista vazia no dicionário,
        # se chave 'v' não existir
        self._lista_de_adjacencias.setdefault(v, [])

        # adiciona a aresta ao vértice 'u'
        self._lista_de_adjacencias[u].append((v, custo))
        if not self.orientado:
            # se é um grafo orientado
            # adiciona a aresta ao vértice 'v'
            self._lista_de_adjacencias[v].append((u, custo))

    def inserir_arestas(self, arestas):
        """Insere todas as arestas no grafo"""
        for aresta in arestas:
            self.inserir_aresta(*aresta)

    def imprimir(self):
        total = 0
        for u, v, custo in self.arestas():
            print("({}, {}, {})".format(u, v, custo), end='')
            total += custo
        if not self.orientado:
            # divide por 2 para descontar a duplicidade
            total = total / 2
        print("")
        print("Custo: {}".format(total))


def dijkstra(grafo, fonte):
    VAZIO = None
    INFINITO = sum([aresta[-1] for aresta in grafo.arestas()])
    antecessor_e_distancia = {}
    fila = {}

    # inicia antecessor_e_custo de todos os vértices
    # com o valor (VAZIO, INFINITO)
    for u in grafo.vertices:
        antecessor_e_distancia[u] = VAZIO, INFINITO
        fila.append(u)

    # inicio
    antecessor_e_distancia[fonte] = VAZIO, 0

    while fila:
        # pega as distâncias de vértices que estão na fila
        selecao_dist_e_vertice = [
            (ant_e_dist[-1], u)
            for u, ant_e_dist, in antecessor_e_distancia.items()
            if u in fila]
        # pega a menor distância dentre elas
        menor_dist, vertice_menor_dist = sorted(selecao_dist_e_vertice)[0]

        # remove vértice u da fila
        fila.remove(vertice_menor_dist)

        # para cada vizinho de vertice_menor_dist
        for v, dist_v in grafo._lista_de_adjacencias[vertice_menor_dist]:
            if v in fila:
                dist = menor_dist + dist_v
                if dist < antecessor_e_distancia[v][1]:
                    antecessor_e_distancia[v] = vertice_menor_dist, dist

    return antecessor_e_distancia


def caminho(antecessor_e_distancia, fonte, destino):
    rota = [destino]
    distancia = antecessor_e_distancia[destino][1]
    while True:
        antecessor = antecessor_e_distancia[destino][0]
        if antecessor is None:
            break
        rota.insert(0, antecessor)
        destino = antecessor
    return "->".join(rota) + " distância: {}".format(distancia)

# INICIO DO PROGRAMA
print( """
Este programa apresenta o custo mínimo para ir
de um ponto A a todos os demais usando o algorítmo de 
Dijkstra.
""")
arestas = [
    ('A', 'B', 3),
    ('A', 'X', 2),
    ('A', 'H', 5),
    ('B', 'C', 4),
    ('B', 'X', 3),
    ('B', 'E', 3),
    ('C', 'H', 3),
    ('C', 'E', 3),
    ('C', 'D', 2),
    ('D', 'G', 3),
    ('D', 'F', 4),
    ('E', 'F', 5),
    ('G', 'H', 5),
]
# cria um objeto Grafo
grafo = Grafo()

# insere as arestas do grafo
grafo.inserir_arestas(arestas)

# executa o algoritmo de Dijkstra
antecessor_e_distancia = dijkstra(grafo, "A")

for u, ant_e_dist in antecessor_e_distancia.items():
    print("De A para {}, distância={}".format(
        u, ant_e_dist[1]
    ))
    print("Caminho {}".format(caminho(antecessor_e_distancia, u, "A")))
