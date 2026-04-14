''' 4. Implemente um algoritmo que receba dois
valores (n1 e n2) e uma lista de valores
inteiros como parâmetros de entrada. A lista
deve ser atualizada inserindo o valor n2 após
o nodo que contém o valor n1. '''

def push_to_next_index_in_list(n1: int, n2: int, lista: list[int]):
    if n1 not in lista:
        return False

    for idx, node in enumerate(lista):
        if node == n1:
            n1_idx = idx
    
    lista += [n2]

    for i in range(len(lista) - 1, n1_idx + 1, -1):
        aux = lista[i-1]
        lista[i-1] = lista[i]
        lista[i] = aux

    return lista

print(push_to_next_index_in_list(3, 7, [1,2,3,4,5]))
