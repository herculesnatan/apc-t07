nota_1, nota_2, nota_3 = map(int, input().split())
media = input()

if media.upper() == 'P':
    tipo_media = "Ponderada"
    peso_1, peso_2, peso_3 = map(int, input().split())
    calcula_media = ((nota_1*peso_1) + (nota_2*peso_2) + (nota_3*peso_3)) / (peso_1+peso_2+peso_3)
elif media.upper() == 'A':
    tipo_media = "Aritmetica"
    calcula_media = (nota_1 + nota_2 + nota_3) / 3
elif media.upper()  == 'H':
    calcula_media = 3 / ((1/nota_1) + (1/nota_2) + (1/nota_3))
    tipo_media = "Harmonica"
else:
    calcula_media = "Operacao inexistente"

print(f'{tipo_media}\n{calcula_media:.2f} ' if isinstance(calcula_media, float) else calcula_media)