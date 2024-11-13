num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

word = str(input())
word_2 = str(input())

# primeira sequencia 
concatena = (num_1 + num_2) * word
concatena_2 = (num_2 + num_3) * word_2
junta_primeiro = concatena + concatena_2
concatena_3 = (num_1 + num_3) * junta_primeiro
print(concatena_3)

