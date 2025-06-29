# 5.4. MAS LENGUAJES DE BUCLE

# smallbad.py

menor_valor = -1
print('Antes', menor_valor)
for valor in [9, 41, 12, 3, 74, 15] :
    if valor < menor_valor :
        menor_valor = valor
    print(menor_valor, valor)

print('Después', menor_valor)
