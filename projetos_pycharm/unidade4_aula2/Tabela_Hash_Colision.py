hashtable = {}
m = 10 # número de índices na tabela

def hashfunct(v,mh): # função hash usando método da divisão
    return v% mh


for i in range (m): # preenchendo indices da tabela
    hashtable[i] = ''


#inserindo números
hashtable[hashfunct(235, m)] = '235'
hashtable[hashfunct(578, m)] = '578'
hashtable[hashfunct(1024, m)] = '1024'
hashtable[hashfunct(96, m)] = '96'
hashtable[hashfunct(32, m)] = '32'

print(hashtable)

# inserção sem tratamento de colisão
hashtable[hashfunct(18, m)] = '18'

print(hashtable)