nomes = [] # criar uma lista vazia
n = int(input())
if n > 0:
    for _ in range(n):
        nome = input()
        nomes.append(nome) # adicionar na lista

    print(*nomes[::-1], sep="\n") # inverter a lista

