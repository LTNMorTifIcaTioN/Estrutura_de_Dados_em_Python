""""
Para que seja simples o entendimento da questão da complexidade vamos considerar o algoritmo de busca sequencial
"""
def buscaSeq(x, elem):
    n = len(x)
    for i in range(0, n):
        if x[i] == elem:
            return 1
    return 0

