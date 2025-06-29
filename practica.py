#a = 0

#while a < 10:
    #a += 1
    #if a == 3:
     #   continue
    #print(a)
        
##tabla = 3
##
##while tabla <= 7:
##    print(f"Tabla del {tabla}")
##    multiplo = 1
##          
##    while multiplo <= 10:
##        print(f"{tabla} X {multiplo} = ", tabla * multiplo)
##
##        multiplo += 1
##
##    print(" ")
##    tabla += 1
##print("###########")

    
##list = ["\U0001F600", "\U0001F40D", "\u2764\uFE0F", "\U0001F9E0", "\U0001F3A8"]
##
##for emoji in list:
##    print(emoji)

##diccionario = {"Nombre":"Rossana", "Apellido":"Liendo", "Altura":"1,80"}
##
##for concepto in diccionario:
##    print(concepto)
##
##for concepto in diccionario:
##    print(concepto, ": ", diccionario[concepto])

dividendo = 1
divisor = 0

try:
    print("Antes del fallo")
    resultado = dividendo / divisor
    print(f"La división resulta: {resultado}")
except:
    if divisor == 0:
        print("No puedes dividir por cero")

print("Programa terminado")
