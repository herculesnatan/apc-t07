PA, PB, T1, T2 = input().split()
PA, PB = int(PA), int(PB)
T1, T2 = float(T1), float(T2)
anos = 0
flag = True
if T2 >= T1:
    print("A nunca alcancara B.")
else:

    while flag:
        PA = int(PA * (T1/100)) + PA
        PB = int(PB * (T2/100) + PB)
        anos += 1
        if PA >= PB and anos <= 1000:
            print(f"Vai alcancar em {anos} ano(s).")
            flag = False
            break
        elif anos > 1000:
            print("Mais de um milenio.")
            flag = False
            break