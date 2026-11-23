### Modules ###

from my_module import printValue, sum # from sirve para importar una función específica de un módulo que se encuentra en el mismo directorio que el archivo que lo importa.

sum(1, 2, 3)
printValue("Hola, mundo!")

import my_module # import sirve para importar un módulo que se encuentra en el mismo directorio que el archivo que lo importa.
#from  10_functions import sum_two_values - No se puede imortar por que el nombre del archivo no es válido, ya que comienza con un número. Los nombres de los archivos deben comenzar con una letra o un guión bajo.

my_module.sum(1, 2, 3) # se puede llamar a la función sum() del módulo module.py usando la sintaxis module.sum().
my_module.printValue("Hola, mundo!")

import math # import sirve para importar un módulo que se encuentra en la biblioteca estándar de Python.
print(math.pi) # se puede llamar a la constante pi del módulo math usando la sintaxis math.pi.
print(math.pow(2, 3)) # se puede llamar a la función pow() del módulo math usando la sintaxis math.pow().