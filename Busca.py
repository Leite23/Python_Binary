def busca(lista, chave):
    for i in range(len(lista)):
        if lista[i] == chave:
            return i
    return -1

lista = [1, 2, 3, 4, 5]
print(busca(lista, 6))