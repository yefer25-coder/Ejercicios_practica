# Filtrar pares
# Crea una función que reciba una lista de números y devuelva solo los pares.

def filter_pair(pairs):
    if not isinstance(pairs, list):
        raise TypeError("You must enter a list of numbers.")
    numbers_pair = []
    for i in pairs:
        if isinstance(i, int):
            if i % 2 == 0:
                numbers_pair.append(i)
    return numbers_pair




# Palíndromo
# Escribe una función que determine si un texto es un palíndromo.

def it_palindrome(text):
    if not isinstance(text, str):
        raise TypeError("It must be text (string).")
    clear_text = ''.join(caracter for caracter in text.lower() if caracter.isalnum())
    inverted_text = clear_text[::-1]
    return  clear_text == inverted_text
pass



# Factorial
# Crea una función que calcule el factorial de un número entero positivo.

def calculate_factory(number):
    if not isinstance(number, int):
        raise TypeError("You must enter a number whole.")
    if number < 0:
        raise ValueError("The number must be higher to zero.")
    if number == 0:
        return 1
    
    result = 1
    for i in range(1, number +1):
        result *= i
    return result
pass




# Eliminar duplicados
# Escribe una función que reciba una lista y devuelva una nueva sin elementos repetidos.

def no_element_repeated(element):
    if not isinstance(element, list):
        raise TypeError("Must be a list.")
    list_no_repeated = []
    for i in element:
        if i not in list_no_repeated:
            list_no_repeated.append(i)
    return list_no_repeated
pass



# FizzBuzz
# Crea una función que reciba un número y devuelva "Fizz", "Buzz" o "FizzBuzz" según las reglas del juego.

def FizzBuzz(number):
    if not isinstance(number, int):
        raise TypeError("The number must be whole.")
    if number % 15 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)
pass


# Contar vocales
# Escribe una función que reciba una cadena y devuelva la cantidad de vocales.

def amount_vowels(string):
    if not isinstance(string, str):
        raise TypeError("It must be a text.")
    vowels_conter = 0
    vowels = "aeiou"
    for i in string:
        i = i.lower()
        if i in vowels:
            vowels_conter += 1
    return vowels_conter




# Invertir texto
# Crea una función que invierta una cadena de texto.

def invert_string(string):
    if not isinstance(string, str):
        raise TypeError("It must be a text.")
    invert = string[::-1]
    return invert
pass
