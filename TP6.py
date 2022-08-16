print("-------------------------------------------------------")
print("VALOR Y RANGO SUPERIOR A 300.")
print("-------------------------------------------------------")

A1 = 1
A2 = 0
An = A1 + (2*A2)

while An < 300:
    A2 = A1
    A1 = An
    An = A1 +(2*A2)
    cont = cont+1

print("El rango es ", cont, " y el resultado es ",An)