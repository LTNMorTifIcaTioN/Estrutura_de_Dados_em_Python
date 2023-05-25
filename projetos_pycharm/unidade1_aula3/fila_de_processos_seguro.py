# Sistema que recebe uma fila de processamento de demandas da empresa de seguros (id numérico)

class Item:
    """insere um item em uma lista"""
    def __init__(self, valor=None, proximo=None):
        self.valor = valor
        self.proximo = proximo

    def __repr__(self):
        return "%s, %s" % (self.valor, self.proximo)

class Fila:
    """Constrói uma fila usando listas encadeadas"""
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
    def __repr__(self):
        return str(self.primeiro)
    def push(self,valor):
        """adiciona itens a fila"""
        item = Item(valor)
        # verifica se existe um item na lista
        if self.primeiro:
            # o valor próximo do ultimo item atual recebe o valor atual do item
            self.ultimo.proximo = item
            self.ultimo = item # a seguir todo o objeto item recebe o item
        # se a lista estiver vazia, então:
        else:
            self.primeiro = item # o item atual se torna o primeiro item
            self.ultimo = item # o item atual também se torna o último item
    def pop(self):
        """remove itens da fila"""
        self.primeiro = self.primeiro.proximo

def main():
    """função principal"""
    # instancia uma nova fila
    fila = Fila()
    print(fila)

    # adicionando itens
    fila.push(1)
    fila.push(2)
    fila.push(3)
    print(fila) # 1, 2, 3, none
    print()

    # removendo itens
    fila.pop()
    print(fila)  # 2, 3, none
    print()

    fila.pop()
    print(fila)  # 3, none

# Executa a função principal
if __name__ == "__main__":
    main()