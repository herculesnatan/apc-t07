valor_fatia = float(3.25)
sabor, numero_fatia = input().split()
numero_fatia = int(numero_fatia)
valor_final = numero_fatia * valor_fatia

frase = "Foram %i pedaços de bolo de %s, então fica %.2f reais"%(numero_fatia, sabor, valor_final)
print(frase)