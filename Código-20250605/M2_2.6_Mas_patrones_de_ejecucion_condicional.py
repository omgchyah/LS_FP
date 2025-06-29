# 3.2. MAS PATRONES DE EJECUCION CONDICIONAL

# Reescribe el programa de salarios usando try y except
# de modo que el programa maneje input (entradas) no numéricas
# de forma correcta.

# Introduce las Horas: 20 
# Introduce la Tarifa: nueve
# Error, por favor, introduce un valor numérico

# Introduce las Horas: cuarenta
# Error, por favor, introduce un valor numérico

while True:

    try:
        horas = float(input('Introduce las Horas: '))
        tarifa = float(input('Introduce la Tarifa: '))
        break

    except ValueError:
        print('Error, por favor, introduce un valor numérico')

if horas >= 40 :
    salario = 40 * tarifa + (horas - 40) * (tarifa * 1.5)
    print(f"Tu salario es: {salario}")
    # print(f"Tu salario es: {40 * tarifa + (horas - 40) * (tarifa * 1.5)}")
else:
    salario = horas * tarifa
    print(f"Tu salario es: {salario}")
    # print(f"Tu salario es: {horas * tarifa}")

