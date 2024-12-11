frase = input()
numero = ""
frase_final = frase

def extenso_para_algarismo(palavra):
    if palavra == "zero":
        return "0"
    elif palavra == "um":
        return "1"
    elif palavra == "dois":
        return "2"
    elif palavra == "três":
        return "3"
    elif palavra == "quatro":
        return "4"
    elif palavra == "cinco":
        return "5"
    elif palavra == "seis":
        return "6"
    elif palavra == "sete":
        return "7"
    elif palavra == "oito":
        return "8"
    elif palavra == "nove":
        return "9"
    elif palavra == "zeroum":
        return "01"
    return None


palavras = frase.split()

for palavra in palavras:
    algarismo = extenso_para_algarismo(palavra)
    if algarismo is not None:
        frase_final = frase_final.replace(palavra, algarismo)

print(frase_final)
