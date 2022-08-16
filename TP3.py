print("-------------------------------------------------------")
print("NÚMEROS PRIMOS:")
print("-------------------------------------------------------")

prim=2
lim=1000
cont=0

for i in range(prim, lim):
    primo = True
    j = 2

    while (i>j) and (primo == True):
        if i%j==0 :
            primo = False
            break
        else:
            j = j+1

    if primo == True :
        print(i, " es primo.")
        cont= cont+1

print("Entre ",prim," y ",lim," hay ",cont," números primos.")