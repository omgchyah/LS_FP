import random

#Ejercicio 1
def how_old_am_i():
    while True:
        try:
            age = int(input("Dime tu edad: "))
            return age
        except ValueError:
            print("Entrada no válida. Introduce un número entero: ")

#Ejercicio 2
def am_i_old_enough():
    age = how_old_am_i()
    
    if age >= 18:
        return "Puedes entrar. Eres mayor de edad.\n"
    else:
        return f"Lo siento. Te faltan {18 - age} años para entrar.\n"

#Ejercicio 3
def classify_grades():
    while True:
        try:
            grade = int(input("Dime tu nota: "))
            if grade <= 4:
                return "Suspenso.\n"
            elif grade == 5:
                return "Aprobado.\n"
            elif grade <= 7:
                return "Bien.\n"
            elif grade <= 9:
                return "Notable.\n"
            else:
                return "Sobresaliente.\n"
        except ValueError:
            print("Entrada no válida. Introduce un número entero: ")

#Ejercicio 4
def guess_number():
    
    num_random = random.randint(1,10)
    num_user = int(input("Introduce un número del 1 al 10: "))

    while True:
        try:
            while num_user != num_random:
                num_user = int(input("Lo siento. Inténtalo de nuevo: "))
            return "Felicidades. Has adivinado el número secreto.\n"    
        except ValueError:
            num_user = int(input("Entrada no válida. Introduce un número entero: "))
                    
#Ejercicio 5
def skip_even_numbers():
    odd_numbers = []
    num_user = int(input("Introduce un número para guardar los impares. Introduce '0' cuando quieras parar: "))
    
    while True:
        try:
            while num_user != 0:
                if num_user % 2 == 0:
                    continue;
                else:
                    odd_numbers.append(num_user)
            num_user = int(input("Introduce otro número (o '0' para terminar): "))
            return odd_numbers
        except ValueError:
            num_user = int(input("Introduce otro número (o '0' para terminar): "))
            
#Ejercicio 6
def add_user_numbers(numbers):
    
    list_strings = str.split(numbers, ",")
    list_valid_numbers = []
    
    for element in list_strings:
        try:
            clean_element = int(element.strip())
            list_valid_numbers.append(clean_element)
        except ValueError:
            continue
    
    return list_valid_numbers

#Ejercicio 7
def verify_age():
    
    age = how_old_am_i()
    
    while age < 0 or age > 120:
        print("La edad no está en el rango válido.")
        age = how_old_am_i()        
        
    if age >= 18:
        return "Eres mayor de edad.\n"
    else:
        return "No eres mayor de edad.\n"

user_option = 0

while user_option != 10:
    
    print("¿Qué deseas hacer?")
    print("1. Saber cuántos años tendré en 10 años.")
    print("2. ¿Puedo entrar en una discoteca?")
    print("3. ¿Cómo me fue en la escuela?")
    print("4. ¡Adivinar el número!")
    print("5. Crear una lista de números impares.")
    print("6. Sumar.")
    print("7. Verificar mi edad.")
    print("8. ¡Adivinar el número! (3 intentos).")
    print("9. Encuenta el primer múltiplo de 7.")
    
    user_option = int(input("Introduce el número de la opción: "))
    
    match user_option:        
        case 1:
            age = how_old_am_i()
            print(f"Tienes {age} años y tendrás {age + 10} años en una década.")
        case 2:
            print(am_i_old_enough())
        case 3:
            print(classify_grades())
        case 4:
            print(guess_number())
        case 5:   
            odd_numbers = skip_even_numbers()
            print("Lista de número impares")
            for num in odd_numbers:
                print(num)
        case 6:
            list = input("Escribe los números a sumar separados por una coma:")
            list_valid_numbers = add_user_numbers(list)
            print(f"The valid numbers are: {list_valid_numbers} and the total sum is {sum(list_valid_numbers)}")
        case 7:
            print(verify_age())         
        # case 8:
        # case 9:
        case 10:
            print("Goobye!")
            break;
        case _:
            print("Opción no válida. Introduzca un número.")
            