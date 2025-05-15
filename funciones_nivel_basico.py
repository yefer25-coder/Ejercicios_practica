# Saludo personalizado
# Crea una función que reciba un nombre y muestre un saludo personalizado.

def to_greet(name):
    if not name.isalpha():
        raise TypeError("You must enter your name.") 
    else:
        return (f"Hellow {name}, how are you? ¡Let is to watch the game!")    
pass




# Suma de dos números
# Escribe una función que reciba dos números y devuelva su suma.

def sum_numbers(number1, number2):
    if not isinstance(number1, (int, float)):
        raise TypeError ("Number one: Enter a number valid.")
    if not isinstance(number2, (int, float)):
        raise TypeError("Number two: Enter a number valid.")
    return number1 + number2
pass




# Número par o impar
# Crea una función que determine si un número es par o impar

def pair_odd(number):
    if not isinstance(number, int):
        raise TypeError("The number aren't valid")
    if number % 2 == 0:
        return "Is pair" 
    else:
        return "Is odd"
pass





# Mayoría de edad
# Escribe una función que reciba una edad y devuelva si es mayor o menor de edad.

def higher_age(age, limit_age = 18):
        if not isinstance(age, int):
            raise TypeError("the age not is validate")
        if age <= 0:
            raise ValueError("Age cannot be negative.")
        if age >= limit_age:
            return "You are higher of age."
        elif age < limit_age:
            return "You are minor of age."   
pass





# Conversor de temperatura
# Crea una función que convierta grados Celsius a Fahrenheit.

def celsius_to_fahrenheit(temperature):
        if not isinstance(temperature, (int, float)):
            raise TypeError("The temperature in not valid.")
        else:
            fahrenheit = (temperature * (9/5)) + 32
        return fahrenheit
pass




# Área de un triángulo
# Escribe una función que devuelva el área de un triángulo dado su base y altura.

def calculate_area_triangle(base, height):
        if not isinstance(base, (int, float)):
             raise TypeError("The base is not a valid number.")
        if not isinstance(height, (int, float)):
             raise TypeError("The height is not a valid number")
        if base < 0 or height < 0:
             raise ValueError("The measures cannot be negative")
        area = (base * height) / 2
        return area
pass




# Mayor de una lista
# Crea una función que reciba una lista de números y devuelva el mayor.

def higher_number(list_number):
    if not list_number:
        return None
    
    list_higher = list_number[0]
    for i in list_number:
        if i > list_higher:
            list_higher = i
    return list_higher
pass
        




# Contar letras
# Escribe una función que cuente cuántas veces aparece una letra en una palabra.

def conter_letter_in_word(word, letter):
    if not isinstance(letter, str) or len(letter) != 1:
        return 0
    word = word.lower()
    letter = letter.lower()
    conter = 0
    for i in word:
        if i == letter:
            conter += 1
    return conter
pass 