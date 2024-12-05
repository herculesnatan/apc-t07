def ePar(num):
    if num % 2 == 0:
        return True

def eImpar(num):
    par = ePar(num)
    if not par:
        return True
    