### Excepctions Handling ###

numberOne = 10
numberTwo = 12
numberThree = "12"

# try es un bloque de código que puede generar una excepción
try:
    print(numberOne + numberTwo)
    print("Suma realizada correctamente")
# except es un bloque de código que se ejecuta si ocurre una excepción
except:
    print("Error: No se puede sumar un número con una cadena de texto")
# else es un bloque de código que se ejecuta si no ocurre ninguna excepción
else:
    print("No hubo errores en la suma")
# finally es un bloque de código que se ejecuta siempre, haya o no error
finally:
    print("Fin del bloque try except else finally")

# Captura de excepciones por tipo de error
try:
    print(numberOne + numberThree)
# TypeError ocurre cuando se intenta realizar una operación entre tipos de datos incompatibles
except TypeError:
    print("Error: Se produjo un error de tipo al intentar sumar un número con una cadena de texto")
# ValueError ocurre cuando se intenta realizar una operación con valores incorrectos
except ValueError:
    print("Error: No se puede sumar un número con una cadena de texto")


#Captura de excepciones por tipo de error y mensaje de error
try:
    print(numberOne + numberThree)
except ValueError as error:
    print("Error: Se produjo un error de valor al intentar sumar un número con una cadena de texto")
    print(error)
except Exception as exception:
    print("Error: Se produjo un error al intentar sumar un número con una cadena de texto")
    print(exception)
