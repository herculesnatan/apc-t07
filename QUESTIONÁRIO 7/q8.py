# Passo 0: receber o n para criar o laço de repetição
n = int(input(""))

# Passo 1: usar o for para receber as strings comprimidas
for _ in range(n):
    string_descomprimida = ""
    letra = ""
    num = 0
    strings_comprimidas = input("")
    tam_string = len(strings_comprimidas)
    
    # Passo 2: "separar" letras de números
    for i in range(tam_string):
        if strings_comprimidas[i].isalpha():
            # Passo 3: definir a nova letra e zerar o num
            letra = strings_comprimidas[i]
            num = 0
        elif strings_comprimidas[i].isnumeric():
            # Passo 4: acomular o número para multiplicar no final
            num = num * 10 + int(strings_comprimidas[i])
            if i == tam_string - 1 or not strings_comprimidas[i + 1].isnumeric():
                string_descomprimida += letra * num

    print(string_descomprimida)
