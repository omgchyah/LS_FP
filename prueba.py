x,y,z = 1, 2, 3
string = "Hola"
#union = x + string
#print(union)

coma_flotante = 3.5

print(type(coma_flotante))

for v in [None, False, 0, 0.0, (1,), 'texto']:
    print(f'{v!r:8} = {bool(v)}')
