# Saludo personalizado
# Crea una función que reciba un nombre y muestre un saludo personalizado.

def to_greet(name):
    if name.isalpha():
        print(f"Hellow {name}, ¡Let is to watch the game!")
    else:
        print("Enter your name.")

# 

# Suma de dos números
# Escribe una función que reciba dos números y devuelva su suma.


# def sum_numbers(number1, number2):
#     return number1 + number2

# def validate_num(str):
#     try: return int(str)
#     except ValueError: return -1


# Número par o impar
# Crea una función que determine si un número es par o impar

# def pair_odd(number):
#     if not number is int(number):
#         return print("The number aren't validate")
#     else:
#         if number % 2 == 0:
#             return print(f"The number {number} is pair.")
#         else:
#             return print(f"The number {number} is odd.")

# number = int(input("Enter a number for to know it is pair or odd: "))
# pair_odd(number)


# Mayoría de edad
# Escribe una función que reciba una edad y devuelva si es mayor o menor de edad.

# def higher_age(age, limit_age = 18):
#         if not age is int(age):
#            return print("The number isn't validate")
#         if age >= limit_age:
#             return print("You are higher of age.")
#         elif age < limit_age:
#             return print("You are minor of age.")     
#         else:
#             if age <= 0:
#                 return print("You must enter your age, it not can be minor to zero.")
       
# age = int(input("You are enter your age: "))  
# higher_age(age)
            



# Conversor de temperatura
# Crea una función que convierta grados Celsius a Fahrenheit.


# def converter_temperature(temperature):
#     entero = int(temperature)
#     flotante = float(temperature)
#     if temperature is entero or temperature is flotante:
#         fahrenheit = (temperature * (9/5)) + 32
#         return print(f"Celsius: {temperature}  to Fahrenheit is: {fahrenheit}")
#     else:
#         return print("Enter a number validate.")


# temperature = float(input("Enter the temperature in celsius for convert in farenheit: "))
# converter_temperature(temperature)


# Área de un triángulo
# Escribe una función que devuelva el área de un triángulo dado su base y altura.

# def calulate_area(base, height):
#     entero = int(base)
#     flotante = float(height)
#     if base is entero or height is flotante:
#         area = (base * height) / 2
#         return area
#     else:
#         print("You must enter a number validate.")
          

# area = input("Enter the base of the triangulo: ")
# altura = input("Enter the height of the triangulo: ")

# print(f"{calulate_area(area, altura):.2f}")


# Mayor de una lista
# Crea una función que reciba una lista de números y devuelva el mayor.

# def heigher_number(list):
#     if not list:
#         return None
    
#     lista = list[0]
#     for i in list:
#         if i > lista:
#             lista = i
#     return lista
        

# lista = [1,2,3,4,13,5,6,7,8,9]
# print(heigher_number(lista))
        

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


print(conter_letter_in_word("yeferson", "e"))