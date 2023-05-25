# Código XX: Classe ItemLista
class ItemLista:
    """Representa cada item de uma lista encadeada"""
    def __init__(self, data=0, nextItem=None):
        self.data = data
        self.nextItem = nextItem
    def __repr__(self):
        return '%s => %s' % (self.data, self.nextItem)

class ListaEncadeada:
    """Cria uma lista encadeada"""
    def __init__(self):
        self.head = None
    def __repr__(self):
        return "%s" % (self.head)
    def insere(lista,data):
        # cria um objeto para armazenar um novo item da lista
        item = ItemLista(data)
        # o head é apontado como próximo item
        item.nextItem = lista.head
        # o item atual se torna o head
        lista.head = item

    # aqui a função busca itens na lista
    def busca(lista,valor):
        navegar = lista.head
        while navegar and navegar.data != valor:
            navegar = navegar.nextItem
        return navegar

    # método de remoção de itens
    def remove(self, valor):
        # verificamos se o item se trata do head
        if self.head.data == valor:
            self.head = self.head.nextItem
        else:
            # detectando a posição do elemento
            before = None
            navegar = self.head
            # navega pelo cabeçalho atual
            while navegar and navegar.data != valor:
                before = navegar
                navegar = navegar.nextItem
            # remove o item atual
            if navegar:
                before.nextItem = navegar.nextItem
            else:
                before.nextItem = None