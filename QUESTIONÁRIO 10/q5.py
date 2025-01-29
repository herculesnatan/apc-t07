mercado = {}
n = int(input())

for i in range(1, n + 1):
    entrada = input().split()
    produtos = entrada[0::2]
    precos = list(map(float, entrada[1::2]))
    mercado[i] = {"produtos": produtos, "precos": precos}

corredor_busca = int(input())

if corredor_busca in mercado:
    produtos = ", ".join(mercado[corredor_busca]["produtos"])
    media = sum(mercado[corredor_busca]["precos"]) / len(mercado[corredor_busca]["precos"])
    print(f"No corredor {corredor_busca} encontramos:")
    print(f"{produtos}")
    print(f"E o preço médio é {media:.2f}.")
else:
    print("Esse corredor não existe no mercado.")
