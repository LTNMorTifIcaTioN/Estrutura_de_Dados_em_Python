pilha = [4, 1, 5, 1, 6]
print(pilha) # [4, 1, 5, 1, 6]
print()
# operação de push com o método append()
pilha.append(10)
print(pilha) # [4, 1, 5, 1, 6, 10]
print()

# operação de pop com método pop()
pilha.pop()
print(pilha) # [4, 1, 5, 1, 6]
print()

# USANDO A ORIENTAÇÃO A OBJETOS

class Pilha: # classe do objeto
    """permite a criação de uma pilha"""
    def __init__(self): # instancia a classe e define os atributos
        self.itens = []
    def __repr__(self): # returna uma mensagem a cada objeto criado, declarando o item adicionado e o próximo item
        return str(self.itens)
    def empilha(self,valor): # função para adicionar os itens na pilha
        """adiciona itens à pilha"""
        self.itens.append(valor)
    def desempilha(self): # função para remover itens na pilha
        assert self.itens, "Erro: pilha vazia."
        # modifica o valor do topo da pilha
        return self.itens.pop()

def main():
    # cria um novo objeto do tipo Pilha
    pilha = Pilha()
    print(pilha)
    print()
    #adiciona um item a pilha
    pilha.empilha(1)
    print(pilha)
    print()
    # remove o item da pilha
    pilha.desempilha()
    print(pilha)
    print()

if __name__=="__main__":
    main()