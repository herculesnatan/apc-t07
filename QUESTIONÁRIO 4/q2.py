count = 0
total_salario = 0
flag = True
while flag:
    nome, salario = input().split(",")
    if nome == 'Fim':
        break
    salario = float(salario)
    count += 1
    total_salario+=salario

if count != 0:
    resultado_final = total_salario / count
    print("%.2f"%resultado_final)
else:
    print("0.00")