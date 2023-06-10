"""
Grafo
"""

class Vertice:
    """Vértice do Grafo"""

    def __init__(self, id, valorado=False):
        # identificação do vértice
        self.id = id
        # vértices vizinhos com seus respectivos custos
        self._vizinhos = dict()
        # valorado ou não
        self._valorado = valorado

    def inserir_adjacente(self, id_vizinho, custo):
        """Insere adjacente"""
        if self._valorado is False:
            custo = 1
        self._vizinhos[id_vizinho] = custo

    @property
    def ids_dos_adjacentes(self):
        """Obtém os ID dos adjacentes"""
        return self._vizinhos.keys()

    def obter_custo(self, id_vizinho):
        """Obtém o custo de um adjacente cujo ID é 'ide_vizinho'"""
        if self._valorado:
            # é valorado, então retorna o custo do dado vizinho
            # se não existir, retornará None
            return self._vizinhos.get(id_vizinho)
        else:
            # não é valorado, então retornará o custo do dado vizinho
            # se não existir, retornará 0
            return self._vizinhos.get(id_vizinho) or 0

    #
class Grafo:
    def __init__(self, direcionado=False, valorado=False):
        # pares chave e valor (id_vertice, objeto do tipo Vértice)
        self._vertices = dict()
        # indica se o grafo é direcionado
        self.direcionado = direcionado
        # indica se o grafo é valorado
        self.valorado = valorado

    def inserir_vertice(self, id_vertice):
        """
        Insere um vértice no grafo, indicando sua indentificação
        """
        # cria um objeto da classe Vértice
        self._vertices[id_vertice] = Vertice(id_vertice, self.valorado)
        # retorna o objeto criado
        return self._vertices[id_vertice]

    def obter_vertice(self, id_vertice):
        """
        Obtém o objeto vértice cuja identificação é 'id_vertice'
        """
        # retorna um objeto da classe Vertice
        # se não existir, retorna None
        return self._vertices.get(id_vertice)

    def _tenta_obter_vertice_senao_cria(self, id_vertice):
        """
        Tenta obter um vértice cuja identificação é 'id_vertice'
        mas se não existir, cria
        """
        return (
            self.obter_vertice(id_vertice) or
            self.inserir_vertice(id_vertice)
        )

    def inserir_aresta(self, id_origem, id_destino, custo=None):
        """
        Cria uma aresta entre os vértices 'id_origem' e 'id_destino'
        'custo' deve ser informado se for um grafo valorado
        """
        if self.valorado and custo is None:
            # exige o custo para o grafo valorado
            raise ValueError("Obrigatório informar custo")

        # cria os vértices se não existirem
        v_origem = self._tenta_obter_vertice_senao_cria(id_origem)
        v_destino = self._tenta_obter_vertice_senao_cria(id_destino)

        # insere 'id_destino' como adjacente de 'v_origem'
        v_origem.inserir_adjacente(id_destino, custo)

        if not self.direcionado:
            # insere 'id_origem' como adjacente de 'v_destino'
            v_destino.inserir_adjacente(id_origem, custo)

    def inserir_arestas(self, arestas):
        """
        Cria todas as arestas de uma única vez e seus vértices
        """
        for aresta in arestas:
            # aresta pode conter (origem, destino)
            # ou (origem, destino, custo)
            self.inserir_aresta(*aresta)

    def imprimir(self, rotulo):
        """Imprime o grafo"""
        ids_ordenados = sorted(self._vertices.keys())
        print("")
        print("{} - Matriz".format(rotulo))
        print("\t" + "\t".join(ids_ordenados))
        for i in ids_ordenados:
            vertice = self.obter_vertice(i)
            print(i, end="|\t")
            for j in ids_ordenados:
                custo = vertice.obter_custo(j) or 0
                print(custo, end="\t")
            print("|")

        print("")
        print("{} - Lista de adjacência".format(rotulo))
        for i in ids_ordenados:
            vertice = self.obter_vertice(i)
            print("| {} |".format(i), end="")
            for j in ids_ordenados:
                custo = vertice.obter_custo(j) or ""
                if custo:
                    apresentacao_custo = ""
                    if self.valorado:
                        apresentacao_custo = " | {}".format(custo)
                    print("->[ {} ]".format(j, apresentacao_custo), end="")
            print("")

#
# INICIO DO PROGRAMA
"""
Figura 3.4
V = {1, 2, 3, 4, 5, 6}
E = {{1,2}, {1,5}, {2,3}, {2,5}, {3,4}, {4,5}, {4,6}}
G = (V(G), E(G))
"""
# sequencias das arestas do grafo
arestas_grafo_fig_3_4 = [
    ('1', '2'),
    ('1', '5'),
    ('2', '3'),
    ('2', '5'),
    ('3', '4'),
    ('4', '5'),
    ('4', '6'),
]
# cria um objeto Grafo, que não é direcionado, que não é ponderado
# e seu nome Grafo fa Figura 3.4
grafo_fig_3_4 = Grafo(
    direcionado=False,
    valorado=False,
)
# insere as arestas
grafo_fig_3_4.inserir_arestas(arestas_grafo_fig_3_4)
# imprime seus dados
grafo_fig_3_4.imprimir("Grafo da Figura 3.4")


"""
Figura 3.3
V = {A, B, C, D, E, F}
E = {{A,B}, {B,C}, {C,D}, {D,E}, {E,F}, {F,D}, {D,A}}
G = (V(G), E(G))
"""
# sequencias das arestas do grafo
arestas_grafo_fig_3_3 = [
    ('A', 'B'),
    ('B', 'C'),
    ('C', 'D'),
    ('D', 'E'),
    ('E', 'F'),
    ('F', 'D'),
    ('D', 'A'),
]
# cria um objeto Grafo, que é direcionado, que não é ponderado
# e seu nome Grafo fa Figura 3.3
grafo_fig_3_3 = Grafo(direcionado=True)
# insere as arestas
grafo_fig_3_3.inserir_arestas(arestas_grafo_fig_3_3)
# imprime seus dados
grafo_fig_3_3.imprimir("Grafo da Figura 3.3")


"""
Figura 3.12
"""
# sequencias das arestas do grafo
arestas_grafo_fig_3_12= [
    ('A', 'B', 10),
    ('A', 'C', -12),
    ('A', 'E', 10),
    ('B', 'C', 5),
    ('B', 'D', -15),
    ('B', 'E', -15),
    ('C', 'D', 5),
    ('C', 'E', -12),
    ('D', 'E', -10),
]
# cria um objeto Grafo, que é direcionado, que é ponderado
# e seu nome Grafo fa Figura 3.12
grafo_fig_3_12 = Grafo(direcionado=True, valorado=True)
# insere as arestas
grafo_fig_3_12.inserir_arestas(arestas_grafo_fig_3_12)
# imprime seus dados
grafo_fig_3_12.imprimir("Grafo da Figura 3.4")