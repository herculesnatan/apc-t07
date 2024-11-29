qnt_pessoas, valor_ingresso = map(int, input().split())
total_arrecadado = 0

for _ in range(qnt_pessoas):
    total_arrecadado += int(input())

media = total_arrecadado / qnt_pessoas
if media >= valor_ingresso:
    print("media: %i\no rock reinara mais uma vez"%media)
else:
    print("media: %i\nrockeiros trabalhando ja"%media)