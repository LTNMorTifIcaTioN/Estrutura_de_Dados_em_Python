dicionario = {
    "A": "Abacate",
    "B": "Bola",
    "C": "Cachorro"
}
# Obtendo o valor da chave correspondente a "A"
print(dicionario["A"]) #Abacate

print()
# navegando pelo dicionário
for chave in dicionario:
    print(chave)

print()
# obter os valores pelo nome do objeto
for chave in dicionario:
    print(chave, dicionario[chave])

print()
# usando keys() e Values() para coletar chave e valor, e zip() para indexar os resultados em uma tupla
for chave, valor in zip(dicionario.keys(), dicionario.values()):
    print(chave, valor)