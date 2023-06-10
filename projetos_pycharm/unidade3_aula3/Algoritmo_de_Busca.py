"""
Algoritmos de Busca em Grafos
"""
class Grafo:

    def __init__(self, orientado=False):
        # dict em que as chaves são o nomes de vértices origem
        # e os valores são os pares de vértice destino
        self._lista_de_adjacencias = dict()
        self.orientado = orientado

    @property
    def vertices(self):
        """Retorna os nomes dos vértices"""
        return set(self._lista_de_adjacencias.keys())

    def arestas(self, v_origem=None):
        """Retorna as arestas do vértice `v_origem` ou do grafo inteiro"""
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
        """Retorna as arestas do vértice `v_origem`"""
        # retorna arestas de um vértice
        arestas = []
        for v_destino in self._lista_de_adjacencias[v_origem]:
            arestas.append((v_origem, v_destino))
        return arestas

    def inserir_aresta(self, u, v):
        """Cria uma aresta entre os vértices `u` e `v`
        """
        # cria uma chave `u` com valor lista vazia no dicionário,
        # se chave `u` não existir
        self._lista_de_adjacencias.setdefault(u, [])

        # cria uma chave `v` com valor lista vazia no dicionário,
        # se chave `v` não existir
        self._lista_de_adjacencias.setdefault(v, [])

        # adiciona a aresta ao vértice `u`
        self._lista_de_adjacencias[u].append(v)
        if not self.orientado:
            # se é um grafo orientado
            # adiciona a aresta ao dicionário do vértice `v`
            self._lista_de_adjacencias[v].append(u)

    def inserir_arestas(self, arestas):
        """Insere todas as arestas no grafo"""
        for aresta in arestas:
            self.inserir_aresta(*aresta)

    def imprimir(self):
        for u, v in self.arestas():
            print("({}, {})".format(u, v), end=' ')
        print("")

    def remover_aresta(self, u, v):
        self._lista_de_adjacencias[u].remove(v)
        if not self.orientado:
            self._lista_de_adjacencias[v].remove(u)

    def remover_vertice(self, u):
        for vertice, vizinhos in self._lista_de_adjacencias.items():
            if u in vizinhos:
                self._lista_de_adjacencias[vertice].remove(u)
        del self._lista_de_adjacencias[u]


def busca_em_profundidade(grafo, vertice_S):
    """
    "Busca em profundidade" percorre o grafo de um ponto e,
    depois um vizinho a partir deste ponto, e repete para
    o vizinho do vizinho
    A ordem é controlada por pilha, colocamos cada vértice na pilha
    E na sua vez, desempilhamos (último a entrar, primeiro a sair)
    """
    # a lista se comporta como pilha se inserimos no final e removemos do final
    # ou inserimos no início e removemos do início
    pilha_STK = list()

    # empilhar vértice S
    pilha_STK.insert(0, vertice_S)

    # controla visitados
    visitados = list()

    while pilha_STK:

        # list.pop(0) remove o primeiro elemento da lista
        # e retorna o valor, ou seja, desempilha
        vertice_U = pilha_STK.pop(0)

        if vertice_U not in visitados:
            # adiciona `vertice_U` à lista de visitados
            visitados.append(vertice_U)

            for vertice_V in grafo._lista_de_adjacencias[vertice_U][::-1]:
                # empilha o vértice V
                pilha_STK.insert(0, vertice_V)

    print("Visitados: {}".format(" -> ".join(visitados)))
    return visitados

def busca_em_largura(grafo, vertice_S):
    """
    "Busca em largura" percorre o grafo de um ponto e de seus vizinhos
    A ordem é controlada por fila, colocamos cada vértice na fila
    E na sua vez, retiramos da fila (primeiro a entrar, primeiro a sair)
    """
    # implementa a fila usando lista e insere o vértice S na lista
    fila_Q = [vertice_S]

    # controla os visitados com uma lista
    visitados = [vertice_S]

    while fila_Q:

        # insere no início e remove do fim
        vertice_U = fila_Q.pop()

        # para cada vértice adjacente de U
        for vertice_V in grafo._lista_de_adjacencias[vertice_U]:

            if vertice_V not in visitados:
                visitados.append(vertice_V)
                fila_Q.insert(0, vertice_V)

    print("Visitados: {}".format(" -> ".join(visitados)))
    return visitados

# INICIO DO PROGRAMA

arestas_grafo = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('B', 'E'),
    ('E', 'H'),
    ('C', 'F'),
    ('C', 'G'),
    ('F', 'I'),
    ('G', 'I'),
    ('G', 'J'),
    ('D', 'J'),
]

# cria um objeto Grafo
grafo = Grafo()
# insere as arestas do grafo
grafo.inserir_arestas(arestas_grafo)

print("Busca em profundidade")
visitados = busca_em_profundidade(grafo, 'A')

print("Busca em largura")
visitados = busca_em_largura(grafo, 'A')

arestas2 = [
    ('A', 'B'),
    ('A', 'D'),
    ('B', 'C'),
    ('B', 'D'),
    ('C', 'D'),
]
grafo2 = Grafo()
grafo2.inserir_arestas(arestas2)
print("Grafo 2")
grafo2.imprimir()
print("Remover (B, D)")
grafo2.remover_aresta('B', 'D')
grafo2.imprimir()

grafo3 = Grafo()
grafo3.inserir_arestas(arestas2)
print("Grafo 3")
grafo3.imprimir()
print("Remover B")
grafo3.remover_vertice('B')
grafo3.imprimir()
