lista = [5,1,2,15,3,20,12,15,11,6]

n = len(lista)

i = 0

while i < n-1:
    m = i

    j = i+1
    while j < n:
        if lista[j] < lista[m]:
            m = j

        j += 1
    print(m)
    if m != i:
        troca = lista[i]
        lista[i] = lista[m]
        lista[m] = troca

    i += 1

print(lista)