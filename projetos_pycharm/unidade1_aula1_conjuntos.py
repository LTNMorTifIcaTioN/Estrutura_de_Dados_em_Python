# o conjunto recebe como entrada uma lista com valores repetidos
conjunto = set([1, 2, 3, 3, 3, 3])
print(conjunto)
# observe que o número 3 se repete na lista, mas ao usar set(), apenas os valores +unicos são incluídos no conjunto.
print()

# podemos adicionar elementos com add()
conjunto.add(777)
print(conjunto)
print()

# podemos remover itens com remove()
conjunto.remove(1)
print(conjunto)
print()

# Realizando operações de união, intersecção e diferença
# declarando dois conjuntos a e b
a = set([1, 2, 3, 4])
b = set([2, 4, 6, 8])

print(a)
print()
print(b)
print()

# união
print(a | b)
print()

# intersecção
print(a & b)
print()

#diferença
print(a-b)
