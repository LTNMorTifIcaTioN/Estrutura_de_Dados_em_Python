"""O seu primeiro desafio será desenvolver a parte de contagem de produtos existentes.
A empresa, apesar de ter diversos produtos diferentes, categoriza os produtos em 15 classes diferentes.
Cada um destes produtos recebe uma identificação própria em etiqueta que possui um número de 10 dígitos,
sendo que os dois últimos números são utilizados para a classe do produto em questão.
Por exemplo, se o produto pertence à classe 1 sua etiqueta terá 10 dígitos e terminará com os números 01."""
import array as arr # biblioteca para tratar arrays

m = 15 # número de índices no hash

# inicialização da tabela como array de inteiros de 15 posições com 0
hashtable = arr.array('i', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

def hashfunct(v, mh): # função hash usando método da divisão
    return v % mh

def insereTC(valor): # incremento do valor do vetor na chave
    hashtable[hashfunct(valor, m)] += 1

def retornaV(valor): # retorna o número de produto para determinada chave
    return hashtable[hashfunct(valor, m)]

# testes
print("C   O   N   T   A   G   E   M      D   E      E   T   I   Q   U   E   T   A   S")

inserir = input("Gostaria de inserir uma etiqueta? S/N: ")
while inserir != 'n' and 'N':
    print(hashtable)
    print()
    x = int(input("Digite o número da etiqueta com 10 algarismos: "))
    insereTC(x)
    print()
    print("Tabela atualizada")
    print(hashtable)
    inserir = input("Gostaria de inserir mais uma etiqueta? S/N: ")

busca = input("Gostaria de buscar uma etiqueta? S/N: ")
while busca != 'n' and 'N':
    x = int(input("Digite uma etiqueta para buscar a quantidade: "))
    print()
    print(retornaV(x))
    busca = input("Gostaria de buscar mais uma etiqueta? S/N: ")