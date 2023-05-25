class Pilha:
    """permite a criação de uma pilha"""
    def __init__(self):
        self.itens = []
    def __repr__(self):
        return str(self.itens)

    def empilha(self, valor):
        """adiciona itens a pilha"""
        self.itens.append(valor)

    def desempilha(self):
        assert self.itens, "Erro: pilha vazia."
        # modifica o valor do topo
        return self.itens.pop()

    def busca(self, alvo):
        """busca por um alvo na pilha"""
        # enquanto houver itens na pilha
        while self.itens:
            # desempilhe o último item
            atual = self.desempilha()
            # verifique se corresponde ao alvo
            if atual == alvo:
                return True # se sim, retorne verdade
            else:
                continue # se não, reinicie o laço while
            return False # caso os itens na pilha acabem, retorne falso

def main():
    #cria um novo objeto do tipo Pilha
    familia = Pilha()

    #adicionando membros da familia
    familia.empilha("Miguel Silva de Castro")
    familia.empilha("José de Castro")
    familia.empilha("Eugênio de Castro")
    familia.empilha("Pedro Paulo de Castro")

    #sabemos que são primos, mas queremos testar se o sistema os encontra
    alvo = "Miguel Silva de Castro"
    parentes = familia.busca(alvo)
    if parentes:
        print("São parentes.")
    else:
        print("Não são parentes.")

if __name__ == "__main__":
    main()