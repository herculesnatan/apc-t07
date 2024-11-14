num_1 = str(input())
num_2 = str(input())
saida_1 = f"I1 = %s, I2 = %s"%(num_1,num_2)
saida_2 = f"I1 = {int(num_1):<10}, I2 = {num_2}"
saida_3 = f"I1 = {num_1}, I2 = {int(num_2):>5}"
saida_4 = f"I1 = {int(num_1):<10}, I2 = {int(num_2):04}"
saida_5 = f"I1 = {num_1.zfill(6)}, I2 = {num_2.zfill(4)}"
print(saida_1, saida_2,saida_3, saida_4, saida_5,sep="\n")

