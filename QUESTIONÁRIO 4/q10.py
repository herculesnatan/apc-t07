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
