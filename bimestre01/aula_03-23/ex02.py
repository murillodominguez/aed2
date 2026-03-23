n = int(input("Informe o tamanho da lista: "))
lista = []
for i in range(n):
    item = int(input(f"Informe o item da posição {i}: "))
    lista.append(item)

target = int(input("Informe um valor para ser buscado na lista: "))
found = False

i = 0
while i < len(lista):
    elem = lista[i]
    if elem == target:
        found = True
        print(f"Valor encontrado! O valor {target} está presenta na lista no endereço {i}.")
        break
    i += 1
    
if not found:
    print(f"O valor {target} não foi encontrado na lista.")
