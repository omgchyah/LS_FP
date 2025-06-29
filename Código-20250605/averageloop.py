# 5.4. MAS LENGUAJES DE BUCLE

# averageloop.py

conteo = 0
suma = 0
print('Antes', conteo, suma)
for valor in [9, 41, 12, 3, 74, 15] :
    conteo = conteo + 1
    suma = suma + valor
    print(conteo, suma, valor)
print('Después', conteo, suma, suma / conteo)
print(f'Después {conteo} {suma} {suma / conteo:.2f}')
