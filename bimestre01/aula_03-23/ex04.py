def count_positives(lista: list):
    counter = 0 
    for i in lista:
        if i > 0:
            counter += 1
    return counter

def count_zeros(lista: list):
    counter = 0
    for i in lista:
        if i == 0:
            counter += 1
    return counter

def count_negatives(lista: list):
    counter = 0
    for i in lista:
        if i < 0:
            counter += 1
    return counter

print(count_positives([0, 2, 3, 4, 5, 6, 7, -2, 4, -3])) # 7
print(count_zeros([0, 2, 3, 4, 5, 6, 0, 2])) # 2
print(count_negatives([0, 1, 3, -3, 2, -1, -509])) # 3