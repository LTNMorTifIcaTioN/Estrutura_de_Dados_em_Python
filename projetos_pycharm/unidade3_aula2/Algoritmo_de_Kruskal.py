"""
Algoritmo de Kruskal
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


def kruskal(grafo):
    # cria conjunto de arestas da MST
    arestas_mst = set()

    # cria um dicionário para armazenar
    # o conjunto de vértices para cada vértice
    # que inicialmente é o próprio vértice
    conjuntos = {v: {v} for v in grafo.vertices}

    # ordena todas as arestas do grafo
    arestas_ordenadas = sorted(
        grafo.arestas(),
        key=lambda aresta: aresta[-1]
    )
    # para cada aresta, em ordem crescente
    for aresta in arestas_ordenadas:
        # obtém u, v e custo, da aresta
        u, v, custo = aresta
        if conjuntos[u].isdisjoint(conjuntos[v]):
            # os conjuntos de u e o de v são conjuntos disjuntos
            # adiciona aresta ao conjunto MST
            arestas_mst.add(aresta)
            # une os conjuntos v e u
            uniao = conjuntos[u] | conjuntos[v]
            # conjunto de u, conterá conjunto de v
            conjuntos[u] = uniao
            # conjunto de v, conterá conjunto de u
            conjuntos[v] = uniao

    mst = Grafo()
    mst.inserir_arestas(arestas_mst)
    return mst


arestas = [
    ('A', 'B', 2),
    ('B', 'C', 4),
    ('A', 'E', 4),
    ('C', 'E', 5),
    ('D', 'E', 2),
    ('D', 'F', 2),
    ('E', 'G', 5),
    ('F', 'G', 5),
]

grafo = Grafo()
grafo.inserir_arestas(arestas)
mst = kruskal(grafo)
mst.imprimir()