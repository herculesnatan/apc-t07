frase = input()
tam_frase = len(frase)
nova_frase = ""
for i in range(tam_frase):
    if i % 2 != 0 and frase[i] != " ":
        nova_frase += frase[i]

print(nova_frase)