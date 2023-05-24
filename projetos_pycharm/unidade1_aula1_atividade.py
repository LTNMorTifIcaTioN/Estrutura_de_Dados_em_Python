# A classe dados deve ser iniciada com uma lista (itens).
# usam-se duas classes especiais, _init_ e _repr_, para instanciar a classe e imprimir valores armazenados.

class Dados:
        """permite a criação de uma estrutura para gravar dados"""
        def __init__(self):
            self.itens = []
        def __repr__(self):
            return str(self.itens)

        # CRIANDO A FUNÇÃO INSERE:
        def insere(self, valor):
            """adiciona itens na lista de dados"""
        # para adicionar um valor na lista usamos o método .append()
            self.itens.append(valor)

        # para remover usamos o método .pop
        def remove(self):
        # modifica o valor do último item
            self.itens.pop()
# testar a classe usando os comandos:
def main():
# CRIANDO UM NOVO OBJETO DO TIPO DADOS
    dados = Dados()

# ADICIONANDO ITENS
    dados.insere(1)
    dados.insere(2)
    dados.insere(3) #último item adicionado
    print()
    print(dados)
    print()

# REMOVENDO ITENS
    dados.remove()
    print(dados)
if __name__ == "__main__":
    main()