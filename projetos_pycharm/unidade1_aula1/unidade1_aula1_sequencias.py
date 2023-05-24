# declarando uma lista numérica
minha_lista = [1, 2, 3, 4, 5]

# imprimindo a lista
print(minha_lista) #[1, 2, 3, 4, 5]

# imprimindo o tipo da variável
print(type(minha_lista))

#imprimindo item por item (usando o índice)
print(minha_lista[0]) #1
print(minha_lista[1]) #2
print(minha_lista[2]) #3
print(minha_lista[3]) #4
print(minha_lista[4]) #5

# Listcomps
# Listcomps, também conhecidos como list compreehension é a forma utilizada da sintaxe Python para criar listas (RAMALHO, 2015).
# O código a seguir lê uma sequência de dez números (de 0 a 9) e armazena os valores pares em uma variável denominada lista:
lista = []
for i in range(10):
    if i % 2 == 0:
        lista.append(i)
print(lista)
# usando listcomp:
numeros_pares = [i for i in range(10) if i%2==0]
print(numeros_pares)