# 5.4. MAS LENGUAJES DE BUCLE

# menorvalor.py

menor = None
print('Antes')
for valor in [9, 41, 12, 3, 74, 15] :
    if menor is None : 
        menor = valor
    elif valor < menor : 
        menor = valor
    print(menor, valor)
print('Después', menor)
