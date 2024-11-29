def fibonacci(n):
    a, b = 0, 1

    for i in range(n):
        if i > 0:
            print(" ", end="")
        print(a, end="")
        a, b = b, a + b
