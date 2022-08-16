print("-------------------------------------------------------")
print("CALCULO DE INTERES:")
print("-------------------------------------------------------")

c = -1
i = -1
m = -1

while (c<0) or (i<=0) or (i>=100) or (m<=0):
    print("Intoduce el capital, el interés y el tiempo apropiados")
    c = float(input("Capital: "))
    i = int(input("Interes: "))
    m = int(input("tiempo: "))

for I in range(m):
    c = c*(1+i/100)

print("Tienes ", c ," soles")