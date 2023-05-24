# Código XX: Classe ItemLista
class ItemLista:
    """Representa cada item de uma lista encadeada"""
    def __init__(self, data=0, nextItem=None):
        self.data = data
        self.nextItem = nextItem
    def __repr__(self):
        return '$s => %s' % (self.data, self.nextItem)

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