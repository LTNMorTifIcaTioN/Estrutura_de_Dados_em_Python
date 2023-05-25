#  CRIANDO A FILA COM A BIBLIOTECA COLLECTIONS.DEQUE
from collections import deque

# usa deque para criar uma fila
fila = deque(["abacate", "bola", "cachorro"])
print(fila) # deque(['abacate', 'bola', 'cachorro'])
print()

# adicionando um novo elemento
fila.append("dado")
print(fila) # deque(['abacate', 'bola', 'cachorro', 'dado'])
print()

# remove o primeiro elemento adicionado à fila
fila.popleft()
print(fila) # deque(['bola', 'cachorro', 'dado'])
print()

# IMPLEMENTANDO A PILHA COMO LISTA ENCADEADA
class Item:
    """insere um item em uma lista"""
    def __init__(self, valor=None, anterior=None):
        self.valor = valor
        self.anterior = anterior
    def __repr__(self):
        return "%s\n%s"% (self.valor, self.anterior)
# cada objeto do tipo item terá dois atributos: valor e anterior
# o método __repr__ retornará o valor atual seguido do valor anterior logo abaixo (placeholders separados por \n)

# IMPLEMENTANDO A CLASSE PILHA
class Pilha:
    """permite a criação de uma pilha"""
    def __init__(self):
        self.topo = None
    def __repr__(self):
        return "TOPO\n%s\nRODAPÉ" % (self.topo)
    # a classe pilha receberá um atributo, topo, que representa o objeto que se encontra no topo da pilha.
    # utiliza-se o método push() para inserir novos valores na pilha
    def push (self, valor):
        # cria um novo objeto Item
        item_novo = Item(valor)
        # o anterior passa a ser o antigo topo
        item_novo.anterior = self.topo
        # o topo da pilha passa a ser o item novo
        self.topo = item_novo
    # três ações são necessárias:
    # 1 - cria-se um novo OBJETO do tipo ITEM enviando o valor que se deseja inserir;
    # 2 - o atributo anterior do novo item dee receber o conteúdo de topo (se for novo recebe None);
    # 3 - a variável topo da pilha deverá recever todo o objeto que armazena o item novo
    # utiliza-se o método pop() para remover os itens da pilha
    def pop (self):
        # verifica se o topo da pilha está vazio
        assert self.topo, "Erro: pilha vazia."
        # modifica o valor do topo
        self.topo = self.topo.anterior

# Este código adiciona quatro itens a lista usando o método push(), e remove dois deles usando o método pop():
def main():
    # cria um novo objeto do tipo pilha
    pilha = Pilha()
    print(pilha)
    print()
    # inserimos alguns valores
    pilha.push('a')
    pilha.push('b')
    pilha.push('c')
    pilha.push('d')
    print(pilha)
    print()
    #removendo os dois últimos itens
    pilha.pop() # remove d
    pilha.pop() # remove c
    print(pilha)
    print()
if __name__ == "__main__":
    main()
