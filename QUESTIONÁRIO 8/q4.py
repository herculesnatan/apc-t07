numeros = list(map(int,(input().split())))

resultado = numeros[0] * 2

for i in range(1, len(numeros)):
    resultado = resultado* 2 + (numeros[i] * 0.5)
    
               
    
print("%.2f"%resultado)

