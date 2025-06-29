# 5.4. MAS LENGUAJES DE BUCLE

# search2.py

found = False
print('Antes', found)
for valor in [9, 41, 12, 3, 74, 15] : 
   if valor == 3 :
       found = True
   print(found, valor)
print('Después', found)
