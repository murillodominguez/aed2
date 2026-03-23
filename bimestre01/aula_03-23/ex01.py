n = 1
lista = []
while n != 0:
    n = int(input("Informe um valor para popular a lista: "))
    if n != 0:
        lista.append(n)

menor = lista[0]
maior = lista[0]
for i in lista:
    if i < menor:
        menor = i
    if i > maior:
        maior = i


print(f"O maior elemento é {maior} e o menor é {menor}")