maior_salario = 0
flag = True
while flag:
    nome, salario = input().split(",")
    salario = float(salario)
    if nome == "Fim":
        break
    if salario > maior_salario:
        maior_salario = salario


if maior_salario != 0:
    print("%.2f"%maior_salario)
else:
    print("Não tem")