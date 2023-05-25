import ListaEncadeada as le
# Cria o objeto
lista = le.ListaEncadeada()
print("Conteúdo da lista: ", lista)
print()
# lista está vazia

# Cria a lista
le.ListaEncadeada.insere(lista, "abacate")
le.ListaEncadeada.insere(lista, "biscoito")
le.ListaEncadeada.insere(lista, "cenoura")
le.ListaEncadeada.insere(lista, "desodorante")
le.ListaEncadeada.insere(lista, "espinafre")
print(lista)
print()
# espinafre => desodorante => cenoura => biscoito => abacate => None

# Realiza uma busca:
query = "cenoura"
item_buscado = le.ListaEncadeada.busca(lista, query)
if item_buscado:
    print("Elemento encontrado")
else:
    print("Elemento não encontrado")
print()
# Neste caso, a busca irá retornar "Elemento Encontrado"

# Realiza a deleção:
print(lista)
print()
# espinafre => desodorante => cenoura => biscoito => abacate => None
le.ListaEncadeada.remove(lista,"cenoura")
print(lista)
# espinafre => desodorante => biscoito => abacate => None