def ehPrimo(n):
    if n < 2:
        return 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    return 1

def divisoresPrimos(n):
    count = 0
    for i in range(1,n-1):
        if n % i == 0 and ehPrimo(i):
            count += 1
    return count

print(ehPrimo(3))
print(ehPrimo(4))
print(ehPrimo(5))
print(ehPrimo(6))
print(ehPrimo(7))
print(ehPrimo(8))
print(ehPrimo(9))
print(ehPrimo(10))
print(ehPrimo(11))
print(ehPrimo(12))
print(ehPrimo(13))
print(ehPrimo(14))
print(ehPrimo(15))
print(ehPrimo(16))
print(ehPrimo(17))
print(ehPrimo(18))
print(ehPrimo(19))
print(ehPrimo(20))
print(ehPrimo(21))
print(ehPrimo(22))
print(ehPrimo(23))
print(ehPrimo(24))
print(ehPrimo(25))
print(ehPrimo(26))
print(ehPrimo(27))
print(ehPrimo(28))
print(ehPrimo(29))

print("/*"*30)
print(divisoresPrimos(3))
print(divisoresPrimos(5))
print(divisoresPrimos(7))
print(divisoresPrimos(11))
print(divisoresPrimos(13))
print(divisoresPrimos(17))
print(divisoresPrimos(19))
print(divisoresPrimos(23))
print(divisoresPrimos(29))
print(divisoresPrimos(31))
print(divisoresPrimos(37))
print(divisoresPrimos(41))
print(divisoresPrimos(43))
print(divisoresPrimos(47))
print(divisoresPrimos(53))
print(divisoresPrimos(59))