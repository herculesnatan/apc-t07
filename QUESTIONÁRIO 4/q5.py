menor_salario = 0
maior_salario = 0
nome_menor_salario = ""
nome_maior_salario = ""
total_salario = 0

n = int(input())
if n == 0:
    print("Não tem média\nNão tem\nNão tem")
else:
    for i in range(n):
        nome, salario = input().split(",")
        salario = float(salario)
        if i == 0:
            menor_salario, maior_salario = salario, salario
            nome_menor_salario, nome_maior_salario = nome, nome
        if salario > maior_salario:
            maior_salario = salario
            nome_maior_salario = nome
        elif salario < menor_salario:
            menor_salario = salario
            nome_menor_salario = nome
        total_salario += salario

    media = total_salario / n
    print(f"{media:.2f}")
    print(f"{nome_maior_salario} {maior_salario:.2f}")
    print(f"{nome_menor_salario} {menor_salario:.2f}")