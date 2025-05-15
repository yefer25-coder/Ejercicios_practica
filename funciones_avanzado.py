# Validar contraseña segura
# Escribe una función que valide si una contraseña cumple con requisitos de seguridad (mayúsculas, minúsculas, números y símbolos).

def valid_password(password):
    if not isinstance(password, str):
        raise TypeError("The password must be a chain of text.")
    
    symbol_rare = "!#$%&'()*+,-./:;<=>?@[]^_`{|}~"
    uppercase = False
    lowercase = False
    numbers = False
    symbol = False
    for character in password:
        if character.isupper():
           uppercase = True
        if character.islower():
            lowercase = True
        if character.isdigit():
            numbers = True
        if character in symbol_rare:
            symbol = True
        if uppercase and lowercase and numbers and symbol:
            break
    return uppercase and lowercase and numbers and symbol
pass




# Simular dado
# Crea una función que simule el lanzamiento de un dado de 6 caras.

import random

def simulate_given():
    dado = random.randint(1,6)
    return dado
pass




# Suma de elementos únicos
# Escribe una función que reciba una lista de números y devuelva la suma de los elementos únicos.

def sum_elements_unique(elements):
    if not isinstance(elements, (list, tuple)):
        raise TypeError("Must be a list o tuple.")
    uniques = []
    for element in elements:
        if not element in uniques:
            uniques.append(element)
    return sum(uniques)
pass



# Generador de contraseñas
# Crea una función que genere una contraseña aleatoria de una longitud dada.

import random 

def generate_password(longitude = 8):
    if not isinstance(longitude, int):
        raise TypeError("The longitude must be a number.")
    if longitude <= 0:
        raise ValueError("The longitude must be higher to zero.")

    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    characters = "!#$%&'()*+,-./:;<=>?@[]^_`{|}~"
    characters_possible = letters + numbers + characters
    sequence = random.choices(characters_possible, k=longitude)
    password_generated = ''.join(sequence)
    return password_generated
pass




# Composición de funciones
# Escribe una función que reciba otra función como parámetro y aplique una composición de funciones.

def split_for(number):
    if not isinstance(number, int):
        raise TypeError("You must enter a number.")
    split = number / 10
    return split
    
def sum_two_number(a, b, function = split_for):
    if not isinstance(a, int) and isinstance(b, int):
        raise TypeError("You must enter a number whole.")
    result = a + b
    return function(result)
pass