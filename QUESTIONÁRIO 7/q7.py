palavra = input()
tam_palavra = len(palavra)
count_diferenca = 0 

for i in range(tam_palavra // 2):
    if palavra[i] != palavra[tam_palavra - i - 1]: # vai pegando cada letra de trás para frente
        count_diferenca += 1

if count_diferenca == 1 or count_diferenca == 0 and tam_palavra % 2 == 1:
    print("ON")
else:
    print("OFF")