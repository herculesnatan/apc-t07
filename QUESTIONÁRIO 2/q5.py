dia, mes, ano = input().split("/")

saida_1 = f"{dia}-{mes}-{ano}"
saida_2 = f"%s-%s-%s"%(mes, dia, ano)
saida_3 = ano + "/" + mes + "/" + dia

print(saida_1, saida_2,saida_3, sep="\n")