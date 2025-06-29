# 5.3. LENGUAJES DE BUCLE

# numero_mayor.py

numero_mayor = None
print('Antes:', numero_mayor)
for objeto in [3, 41, 12, 9, 74, 15]:
    if numero_mayor is None or numero_mayor < objeto:
        numero_mayor = objeto
    print('Bucle:', objeto, numero_mayor)
print('Número mayor:', numero_mayor)
