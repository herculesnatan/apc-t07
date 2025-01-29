lista = list(map(int, input().split()))
fatiamento = list(map(int, input().split()))

fatia = lista[fatiamento[0]:fatiamento[1]]
print(fatia)