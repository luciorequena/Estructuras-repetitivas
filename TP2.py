print("-------------------------------------------------------")
print("SUMA DE DIVISORES:")
print("-------------------------------------------------------")

print("Ingrese números aleatorios, para concluir, ingrese un número negativo")

num = int(input())

while (num > 0):
    suma = 0

    for i in range (1,num+1):
        if num % i==0:
            suma = suma + i
    
    print("La suma de los divisores del número es: ", suma)

    print("Ingrese números aleatorios, para concluir, ingrese un número negativo")
    num= int(input())