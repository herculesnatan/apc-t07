frase = input()
tam_frase = len(frase)
count = 0
for i in range(tam_frase):
    if frase[i].isdigit():
        count += 1
    
print(count)
