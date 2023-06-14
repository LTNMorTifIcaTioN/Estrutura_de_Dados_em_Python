hashtable = {}
m = 10 # número de índices na tabela

def hashfunct(v,mh): # função hash usando método da divisão
    return v% mh

def insereTC(valor):
    if (hashtable[hashfunct(valor, m)]==''):
        hashtable[hashfunct(valor, m)] = valor
    else:
        print("Colisão detectada, tratar colisão...")

for i in range (m): # preenchendo indices da tabela
    hashtable[i] = ''


#inserindo números
insereTC(235)
insereTC(578)
insereTC(1024)
insereTC(96)
insereTC(32)

print(hashtable)

# inserção com tratamento de colisão
insereTC(18)

print(hashtable)