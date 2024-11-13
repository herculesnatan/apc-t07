char_1 = str(input())
char_2 = str(input())
char_3 = str(input())

saida_1 = (f'{char_1}{char_2}{char_3}')
saida_2 = (f'{char_1}')
saida_3 = (f'{char_2*2}')
saida_4 = (f'{char_3} {char_3} {char_3}')
saida_5 = (f'X == {char_1}, Y == {char_2}, Z == {char_3}')
saida_6 = (f'X != {char_2}, Y != {char_1}, Z == {char_3}')

print(saida_1, saida_2, saida_3, saida_4, saida_5, saida_6, sep="\n")