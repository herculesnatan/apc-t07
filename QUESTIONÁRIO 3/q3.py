import math
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

distancia = math.sqrt((x1-x2)**2  +(y1-y2)**2)

if distancia <= 100: 
    frase = "É o amor da minha vida!"
elif distancia <= 200:
    frase = "Talvez dê certo"
else:
    frase = "Não vale a pena investir"

print(frase)