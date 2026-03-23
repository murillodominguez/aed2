lista_sal = []

i = 0
while i < 12:
    sal = float(input(f"Informe um salário ({i+1}/12): "))
    lista_sal.append(sal)
    i += 1

for i, sal in enumerate(lista_sal):
    if sal > 5000:
        print(f"No mês {i} a pessoa ganhou mais que 5000 reais.")
    
    if i > 0 and sal_anterior < sal:
        print(f"O mês {i} teve aumento de salário em relação ao mês anterior. {sal} - {sal_anterior} = R${(sal - sal_anterior):.2f} de aumento")
    
    sal_anterior = i