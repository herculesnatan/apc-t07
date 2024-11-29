num = int(input())

if num == 0:
    print(0)
else:
    for i in range(num+1):
        if i % 3 == 0 and i % 7 == 0:
            print(i, end=" ")