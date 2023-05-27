# Árvore n-nária ca+az de indicar filmes pela classificação etária.

class Filme:
    def __init__(self, nome, classificacao_etaria):
        self.nome = nome
        self.classificacao_etaria = classificacao_etaria

class No:
    def __init__(self, filme):
        self.filme = filme
        self.filhos = []

class Arvore:
    def __init__(self):
        self.raiz = None

    def adicionar_no(self, no_pai, no_filho):
        no_pai.filhos.append(no_filho)

    def percorrer_pre_ordem(self, no):
        print(no.filme.nome)
        for filho in no.filhos:
            self.percorrer_pre_ordem(filho)

class main():
    arvore = Arvore()
    raiz = No(Filme("Filme 1", "livre"))
    arvore.raiz = raiz

    no_1 = No(Filme("Filme 2", "a partir de 10 anos"))
    no_2 = No(Filme("Filme 3", "a partir de 12 anos"))
    no_3 = No(Filme("Filme 4", "a partir de 14 anos"))
    no_4 = No(Filme("Filme 5", "a partir de 16 anos"))
    no_5 = No(Filme("Filme 6", "a partir de 18 anos"))

    arvore.adicionar_no(raiz, no_1)
    arvore.adicionar_no(raiz, no_2)
    arvore.adicionar_no(raiz, no_3)
    arvore.adicionar_no(raiz, no_4)
    arvore.adicionar_no(raiz, no_5)

    no_6 = No(Filme("Filme 9234", "a partir de 18 anos"))
    no_7 = No(Filme("Filme 1234", "a partir de 18 anos"))
    no_8 = No(Filme("Filme 162", "a partir de 16 anos"))
    no_9 = No(Filme("Filme 161", "a partir de 16 anos"))
    no_10 = No(Filme("Filme 143", "a partir de 14 anos"))
    no_11 = No(Filme("Filme 142", "a partir de 14 anos"))
    no_12 = No(Filme("Filme 141", "a partir de 14 anos"))

    arvore.adicionar_no(raiz, no_6)
    arvore.adicionar_no(raiz, no_7)
    arvore.adicionar_no(raiz, no_8)
    arvore.adicionar_no(raiz, no_9)
    arvore.adicionar_no(raiz, no_10)
    arvore.adicionar_no(raiz, no_11)
    arvore.adicionar_no(raiz, no_12)

    arvore.percorrer_pre_ordem(raiz)

if __name__ == "__main__":
    main()