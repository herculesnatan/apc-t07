letras = {
    "d": 0,
    "t": 0,
    "v": 0
}

frase = input()

for palavra in frase:
    if palavra == "d":
        letras["d"] += 1
    elif palavra == "t":
        letras["t"] += 1
    elif palavra == "v":
        letras["v"] += 1


for key, value in letras.items():
    if value != 0:
        print(key,value)
