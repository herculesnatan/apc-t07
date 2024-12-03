def areas(a, b, c):
    a, b, c = int(a), int(b), int(c)
    retangulo_1 = a * b
    retangulo_2 = (b * c)/2
    retangulo_3 = ((b + c)*a)/2
    print(retangulo_1, int(retangulo_2), int(retangulo_3), sep="\n")