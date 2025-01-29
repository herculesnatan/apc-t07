numeros = list(map(int, input().split()))
divisores = int(input())

for i in range(len(numeros)):
    if numeros[i] % divisores == 0:
        print(numeros[i], end=" ")