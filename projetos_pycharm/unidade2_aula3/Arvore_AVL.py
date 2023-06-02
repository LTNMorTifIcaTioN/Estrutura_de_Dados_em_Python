from random import choice

class VerticeAVL:
    """
    Vertice de Árvore Binária AVL
    """

    def __init__(self, chave, dado, pai=None):
        # será usada na busca
        self.chave = chave
        self.dado = dado
        # vértice pai
        self.pai = pai
        # filho menor (à esquerda) e maior (à direita)
        self.menor = None
        self.maior = None

    def __str__(self):
        return str(self.chave)

    def apresentar(self, num_espacos=0, sentido=""):
        espacos = " " * num_espacos
        if self.menor:
            self.menor.apresentar(num_espacos + 10, sentido="/")

        print("{}{}----> [{}]".format(espacos, sentido, self.chave))

        if self.maior:
            self.maior.apresentar(num_espacos + 10, sentido="\\")

    def representacao_com_parenteses(self):
        """
        Retorna a representação da árvore com aninhamento por parênteses
        :return: (str)
        """
        dir = esq = ""
        if self.menor:
            # recursividade
            esq = self.menor.representacao_com_parenteses()

        if self.maior:
            # recursividade
            dir = self.maior.representacao_com_parenteses()

        return "({}{}{})".format(str(self), esq, dir)

    def representacao_com_recuo(self, numero_de_espacos=0):
        """
        Retorna a representação da árvore com recuo
        :return: (str)
        """
        esq = dir = ""
        if self.menor:
            esq = self.menor.representacao_com_recuo(numero_de_espacos + 4)

        if self.maior:
            dir = self.maior.representacao_com_recuo(numero_de_espacos + 4)

        return "{esq}{espacos}{self}\n{dir}".format(
            espacos=' ' * numero_de_espacos, self=str(self), esq=esq, dir=dir,
        )

    def inserir(self, chave_nova, dado):
        """
        Executa a inserção
        :param chave_nova: chave da chave a ser inserido
        :return: vértice inserido
        """

        if chave_nova == self.chave:
            return self
        raiz_da_subarvore = self
        if chave_nova < self.chave:
            # é menor, procura no lado esquerdo
            if self.esquerdo:

                raiz_da_subarvore = self.esquerdo.inserir(chave_nova, dado)
            else:
            # cria Vertice no lado menor
                self.esquerdo = VerticeAVL(chave_nova, dado, self)
            # retorna vertice criado

        elif chave_nova > self.chave:
            # é maior, procura no lado direito
            if self.direito:

                raiz_da_subarvore = self.direito.inserir(chave_nova, dado)

            else:
            # cria Vertice no lado maior e o retorna
                self.direito = VerticeAVL(chave_nova, dado, self)
            # retorna vertice criado
        raiz_da_subarvore.atualizar_altura()
        raiz_da_subarvore = raiz_da_subarvore.balancear()
            # encontrou, retorna o próprio, não faz inserção
        return raiz_da_subarvore.pai or raiz_da_subarvore

    def _remover_folha(self):
        """
        Remove o vértice folha
        :return: vértice removido
        """
        print("Remover FOLHA. Sou folha")
        if self.pai:
            # tem pai, então não sou a raiz
            if self.pai.menor is self:
                # sou filho da esquerda, me desvincula da esquerda
                self.pai.menor = None
            else:
                # sou filho da direita, me desvincula da direita
                self.pai.maior = None
            # me desvinculo do meu pai
            self.pai = None
        # retorna o vértice removido
        return self

    def _remover_pai_de_um_filho(self):
        """
        Remove o vértice que tem um filho seja à direita ou à esquerda
        :return: vértice removido
        """
        print("Remover PAI de 1 filho. Sou pai de 1 filho")
        # identifico meu pai
        meu_pai = self.pai
        # tenho só 1 filho, identifico meu filho (esquerdo ou direito)
        meu_filho = self.menor or self.maior

        if meu_pai is None:
            # sou raiz, a árvore está apontando para mim,
            # não posso ser removido
            # então, vou trocar de lugar com meu filho
            meu_filho.chave, self.chave = self.chave, meu_filho.chave

            # agora estou no lugar do meu filho e posso ser removido
            # a recursividade tratará a forma como serei removido
            return meu_filho.remover(meu_filho.chave)

        # meu pai, é pai do meu filho
        meu_filho.pai = meu_pai

        # meu filho, passa a ser filho do meu pai
        if meu_pai.menor is self:
            # sou filho da direita,
            # meu filho passa a ser seu filho da direita
            meu_pai.menor = meu_filho
        else:
            # sou filho da esquerda,
            # meu filho passa a ser seu filho da esquerda
            meu_pai.maior = meu_filho

        # me desvinculo do meu pai e do meu filhho
        self.pai = None
        self.menor = None
        self.maior = None
        return self

    def _remover_pai_de_dois_filhos(self):
        """
        Remove o vértice que tem 2 filhos
        :return: vértice removido
        """
        print("Remover PAI de 2 filhos. Sou pai de 2 filhos")
        # sou pai de dois filhos

        # obter o menor do lado menor
        menor = self.maior.buscar_menor()

        # troca valor da chave entre o nó atual e o menor
        self.chave, menor.chave = menor.chave, self.chave

        # remover o menor / recursividade
        return menor.remover(menor.chave)

    def remover(self, chave):
        print("Remover {} (chave atual: {})".format(chave, self.chave))
        if self.chave == chave:
            print("Achou{} para remover".format(chave))

            if self.esquerdo and self.direito:
                raiz_da_subarvore = self._remover_pai_de_dois_filhos()
            elif self.esquerdo or self.direito:
                raiz_da_subarvore = self._remover_pai_de_um_filho()
            else:
                raiz_da_subarvore = self._remover_folha()
            return raiz_da_subarvore

        raiz_da_subarvore = self
        if chave < self.chave:
            raiz_da_subarvore = self.esquerdo and self.esquerdo.remover(chave)
        elif chave > self.chave:
            raiz_da_subarvore = self.direito and self.direito.remover(chave)

        if raiz_da_subarvore:
            raiz_da_subarvore.atualizar_altura()
            raiz_da_subarvore = raiz_da_subarvore.balancear()
        return raiz_da_subarvore.pai or raiz_da_subarvore

    def imprimir_percurso_em_ordem(self):
        """
        Percorre a árvore em ordem simétrica (esquerda, vértice, direita)
        e imprime a chave do vértice
        :return: None
        """
        if self.menor:
            # recursividade: executa o mesmo atributo para seu filho esquerdo
            self.menor.imprimir_percurso_em_ordem()
        # imprime a chave do vértice
        print(self)
        if self.maior:
            # recursividade: executa o mesmo atributo para seu filho direito
            self.maior.imprimir_percurso_em_ordem()

    def imprimir_percurso_pre_ordem(self):
        """
        Percorre a árvore em pré ordem (vértice, esquerda, direita)
        e imprime a chave do vértice
        :return: None
        """
        # imprime a chave do vértice
        print(self)
        if self.menor:
            # recursividade: executa o mesmo atributo para seu filho esquerdo
            self.menor.imprimir_percurso_pre_ordem()
        if self.maior:
            # recursividade: executa o mesmo atributo para seu filho direito
            self.maior.imprimir_percurso_pre_ordem()

    def imprimir_percurso_pos_ordem(self):
        """
        Percorre a árvore em pré ordem (esquerda, direita, vértice)
        e imprime a chave do vértice
        :return: None
        """
        if self.menor:
            # recursividade: executa o mesmo atributo para seu filho esquerdo
            self.menor.imprimir_percurso_pos_ordem()
        if self.maior:
            # recursividade: executa o mesmo atributo para seu filho direito
            self.maior.imprimir_percurso_pos_ordem()
        # imprime a chave do vértice
        print(self)

    def buscar(self, chave_nova):
        print("")
        print("Procurando {}. Chave atual: {}".format(chave_nova, self.chave))
        if chave_nova < self.chave:
            return self.menor and self.menor.buscar(chave_nova)
        elif chave_nova > self.chave:
            return self.maior and self.maior.buscar(chave_nova)
        else:
            # encontrou, retorna o próprio
            return self

    def buscar_menor(self):
        """
        Procura o menor até que não encontra e
        retorna ele mesmo
        """
        print("Procurar menor {}".format(self))
        if self.menor:
            # recursividade
            return self.menor.buscar_menor()
        return self

    def imprimir(self):
        if self.menor:
            self.menor.imprimir()
        print("{}|\t{}".format(self.chave, self.dado))
        if self.maior:
            self.maior.imprimir()

    @property
    def altura(self):
        return self._altura

    def atualizar_altura(self):
        self._altura = 1 + max([self.altura_esquerda, self.altura_direita])

    @property
    def altura_esquerda(self):
        if self.esquerdo:
            return self.esquerdo.altura
        return -1

    @property
    def altura_direita(self):
        if self.direito:
            return self.direito.altura
        return -1

    def balancear (self):
        fb = self.fator_de_balanceamento
        print("fb({})={}".format(self.chave, fb))
        if fb == 2:
            return self._balancear_subarvore_direita()
        if fb == -2:
            return self._balancear_subarvore_esquerda()
        return self

    def _balancear_subarvore_direita(self):
        """Resolve casos RR e RL"""
        print("Balancear subarvore direita de {}". format(self.chave))
        if self.direito.fator_de_balanceamento == -1:
            print("Caso RL: Rotação de {} à direita + Rotação de {} à esquerda".format(
                str(self.direito), self.chave)
            )
            self.direito._rotacao_para_direita()
        # Caso RR:
        nova_raiz = self._rotacao_para_esquerda()
        return nova_raiz

    def _balancear_subarvore_esquerda(self):
        """Resolve casos LL e LR"""
        print("Balancear subarvore esquerda de {}". format(self.chave))
        if self.esquerdo.fator_de_balanceamento == 1:
            print("Caso RL: Rotação de {} à esquerda + Rotação de {} à direita".format(
                str(self.esquerda), self.chave)
            )
            self.esquerdo._rotacao_para_esquerda()
        # Caso LL:
        nova_raiz = self._rotacao_para_direita()
        return nova_raiz

    def _rotacao_para_esquerda(self):
        self._rotacao_info("esquerda")
        raiz_da_subarvore = self
        pai_da_subarvore = raiz_da_subarvore
        v1 = raiz_da_subarvore
        v2 = v1.direito
        s2 = v2.esquerdo

        if pai_da_subarvore:
            if raiz_da_subarvore is pai_da_subarvore.direito:
                pai_da_subarvore.direito = v2
            else:
                pai_da_subarvore.esquerdo = v2
        v1.pai = v2
        v1.direito = s2
        v2.pai = pai_da_subarvore
        v2.esquerdo = v1
        if s2:
            s2.pai = v1

        v1.atualizar_altura()
        v2.atualizar_altura()

        self._rotacao_info("esquerda", v2)

        return v2

    def _rotacao_para_direita(self):
        self._rotacao_info("esquerda")
        raiz_da_subarvore = self
        v3 = raiz_da_subarvore
        pai_da_subarvore = raiz_da_subarvore
        v2 = v3.esquerdo
        s3 = v2.direito

        if pai_da_subarvore:
            if raiz_da_subarvore is pai_da_subarvore.direito:
                pai_da_subarvore.direito = v2
            else:
                pai_da_subarvore.esquerdo = v2
        v2.pai = pai_da_subarvore
        v2.direito = v3
        v3.pai = v2
        v3.esquerdo = s3
        if s3:
            s3.pai = v3

        v3.atualizar_altura()
        v2.atualizar_altura()

        self._rotacao_info("direita", v2)

        return v2
class ArvoreAVL:

    def __init__(self):
        self._raiz = None

    def inserir(self, chave, dado):
        if self._raiz is None:
            self._raiz = VerticeAVL(chave, dado)
        else:
            self._raiz = self._raiz.inserir(chave, dado)
        self._raiz.imprimir()

    def remover(self, chave):
        if self._raiz is not None:
            self._raiz = self._raiz.remover(chave)
        self._raiz.imprimir()

    def imprimir(self):
        # 3 formas de apresentar a árvore como está neste momento
        if self._raiz:
            self._raiz.imprimir()

class ListaDeAfazeres:

    def __init__(self):
        self.arvore = ArvoreAVL()

    def inserir(self, ordem, atividade):
        self.arvore.inserir(ordem, atividade)

    def remover(self, ordem):
        self.arvore.remover(ordem)

    def listar(self):
        print("_"*20)
        print("Seus afazeres são: ")
        self.arvore.imprimir()
        print("_"*20)

# Criação do objeto
lista_de_afazeres = ListaDeAfazeres()

while True:
    try:
        lista_de_afazeres.listar()
        # op = input("Digite I para inserir ou R para Remover Atividade: ")
        op = input(
            """
            Digite i para Inserir atividade
            Digite r para Remover atividade
            Digite X para Sair
            """
        )
        print(op)
        if op == "x":
            print("Saiu do programa")
            break

        if op == "i":
            atividade = input("Entre com a atividade: ")
            ordem = int(input("Entre com a ordem (número): "))
            lista_de_afazeres.inserir(ordem, atividade)
            continue

        if op == "r":
            ordem = int(input("Entre com a ordem (número): "))
            lista_de_afazeres.remover(ordem)
            continue

    except Exception:
        print("Terminado pelo usuário")
        break