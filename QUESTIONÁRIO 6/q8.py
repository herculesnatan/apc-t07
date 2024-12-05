def deivis_sequence(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    else:
        return (deivis_sequence(num - 1)  + deivis_sequence(num - 2)) - 1

print(deivis_sequence(10))