catalogo = input().split()
catalogo_items = {}
tam = len(catalogo)


for i in range(0, tam, 2):
    catalogo_items[catalogo[i]] = float(catalogo[i + 1])

items_escolhidos = input().split()
total = 0

for i in range(0, len(items_escolhidos), 2):
    item = items_escolhidos[i]
    quantidade = int(items_escolhidos[i + 1])
    total += catalogo_items[item] * quantidade

print(f"R$ {total:.2f}")


