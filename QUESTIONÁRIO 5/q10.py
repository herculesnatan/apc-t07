def troco(n):
    n = float(n)
    troco_50 = n // 50
    resto_troco_50 = n % 50

    troco_25 = resto_troco_50 // 25
    resto_troco_25 = resto_troco_50 % 25

    troco_10 = resto_troco_25 // 10
    resto_troco_10 = resto_troco_25 % 10

    troco_5 = resto_troco_10 // 5
    resto_troco_5 = resto_troco_10 % 5

    troco_1 = resto_troco_5 // 1
    
    print(f"{int(troco_50)} moedas de 50 centavos\n{int(troco_25)} moedas de 25 centavos\n{int(troco_10)} moedas de 10 centavos\n{int(troco_5)} moedas de cinco centavos\n{int(troco_1)} moedas de 1 centavo")

