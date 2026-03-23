n = int(input("Insira um inteiro n: "))

i = n-1

divisores = [n]

while i > 0:
    if n%i == 0:
        divisores.append(i)

    i -= 1

print(divisores)