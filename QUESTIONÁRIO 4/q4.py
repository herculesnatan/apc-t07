menor_salario = 0
nome_menor_salario = ""
flag = True
while flag:
    nome, salario = input().split(",")
    salario = float(salario)
    if nome == "Fim":
        break
    if nome_menor_salario == "":
        menor_salario = salario
        nome_menor_salario = nome
    elif salario < menor_salario:
        menor_salario = salario
        nome_menor_salario = nome

if menor_salario != 0:
    print(nome_menor_salario)
else:
    print("Não tem")