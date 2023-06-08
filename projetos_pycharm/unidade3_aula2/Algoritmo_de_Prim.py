"""
Algoritmo de Prim
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


def prim(grafo, inicio):
    """
    PRIM(G):
    MST = {INICIO}
    ENQUANTO MST.V ≠ G.V:
    aresta (u, v) de menor peso tal que u ∈ MST.V e v ∈ G.V – MST.V
    MST = MST Ս {(u, v)}
    retorna MST
    """
    # CRIA UMA mst VAZIA
    mst = Grafo(True)
    mst.inserir_aresta(inicio, inicio, 0)
    ordenadas = []

    # atualizar o vértice atual com o vértice inicial
    v = inicio

    while set(mst.vertices) != set(grafo.vertices):
        print()
        MST_V = mst.vertices
        G_V_menos_MST_V = grafo.vertices - mst.vertices
        print("MST.V = {}".format(MST_V))
        print("G.V - MST.V = {}".format(G_V_menos_MST_V))

        print("Vértice atual: {}".format(v))

        # soma as arestas existentes na fila com
        # as arestas do vértice atual e reordena
        print("Insere na fila as arestas que partem de {}".format(v))
        ordenadas = sorted(
            set(ordenadas + grafo.arestas(v)),
            key=lambda aresta: aresta[-1])

        # obtém o vértice de menor custo, que seja válido
        # aresta (u, v) de menor peso tal que u está em MST.V e v está em G.V - MST.V
        print("Procura na fila a primeira aresta(u,v) "
              "de menor peso tal que u pertence a {} e v pertence a {}".format(MST_V, G_V_menos_MST_V))
        for aresta in ordenadas:
            # obtém a próxima aresta de menor custo
            # e que atenda a restrição
            u, v, custo = aresta
            if u in mst.vertices and v not in mst.vertices:
                print("Remove aresta {} da fila".format(aresta))
                ordenadas.remove(aresta)
                print("Insere aresta {} na MST".format(aresta))
                mst.inserir_aresta(u, v, custo)
                # encontrou, interrompe a repetição
                break
    return mst

# INICIO DO PROGRAMA
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
mst = prim(grafo, "G")
mst.imprimir()