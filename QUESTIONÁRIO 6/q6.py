def raizes(a, b, c):
    bahkara = (b**2) - 4*a*c
    if bahkara < 0:
        return -1
    else:
        x1 = (-b + bahkara**(1/2) / (2*a))
        x2 = (-b - bahkara**(1/2) / (2*a))
        if x1 == x2:
            return 1
        else:
            return 2
