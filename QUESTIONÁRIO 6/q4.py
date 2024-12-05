def max2(a,b):
    if a>b:
        return a
    else:
        return b

def max3(a,b, c):
    chama_max = max2(a,b)
    if chama_max > c:
        return chama_max
    else:
        return c