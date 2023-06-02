# Exemplo de Árvore QuadTree para compactação de imagens

"""
Em Quadtree.__init__, implementado nas linhas 10 a 15,
instancia os atributos self.NO, self.NE, self.SE, self.SO,
e self._altura com valores padrão.
"""
class QuadTree:

    def __init__(self, altura=None):
        self.NO = None
        self.NE = None
        self.SO = None
        self.SE = None
        self._altura = altura or 0

    """
    Em Quadtree.inserir_vertice, definido nas linhas 25 a 38,
    obtemos um código da imagem com as cores mescladas,
    fazemos a divisão da imagem em 4 quadrantes (linha 28).
    Se estas quatro imagens tiverem cores diferentes entre si (linha 29),
    criamos os filhos para compor os atributos self.NO,
    self.NE, self.SE, self.SO que serão objetos da classe Quadtree.
    """
    def inserir_vertice(self, img):
        self.imagem_com_cores_mescladas = obter_imagem_com_cores_mescladas(img)
        imagem_dividida = dividir_em_4(img)
        if imagens_diferentes(imagem_dividida):
            h = self._altura + 1
            self.NO = QuadTree(h)
            self.NE = QuadTree(h)
            self.SO = QuadTree(h)
            self.SE = QuadTree(h)
            self.NO.inserir_vertice(imagem_dividida[0])
            self.NE.inserir_vertice(imagem_dividida[1])
            self.SO.inserir_vertice(imagem_dividida[2])
            self.SE.inserir_vertice(imagem_dividida[3])
        return self

    """
    Em Quadtree.obter_vertice, definido nas linhas 48 a 55,
    retornamos a imagem formada pelos quadrantes de uma dada altura
    ou de um vértice folha (linhas 49 e 50). Senão,
    retornamos o resultado da concatenação das imagens daquela altura da Quadtree,
    executando recursivamente o atributo Quadtree.obter_vertice
    para cada quadrante NO, NE, SO, SE.
    """
    def obter_vertice(self, altura):
        if self.folha or self._altura == altura:
            return self.imagem_com_cores_mescladas
        return concatenar(
            self.NO.obter_vertice(altura),
            self.NE.obter_vertice(altura),
            self.SO.obter_vertice(altura),
            self.SE.obter_vertice(altura)
        )