nota_1, nota_2, nota_3 = map(float, input().split())
peso_1, peso_2, peso_3 = map(int, input().split())

calcula_media = ((nota_1*peso_1) + (nota_2*peso_2) + (nota_3*peso_3)) / (peso_1+peso_2+peso_3)
print(f'%.6f' % calcula_media)