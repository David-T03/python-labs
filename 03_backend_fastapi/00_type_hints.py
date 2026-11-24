### Type Hints in FastAPI ###

# Definimos una variable strig
my_string_variable = "Hello, FastAPI!"
print(my_string_variable)
print(type(my_string_variable))

# Redefinimos la variable como un entero
my_string_variable = 5
print(my_string_variable)
print(type(my_string_variable))

# Definimos una variable con type hints
my_string_variable: str = "Hello, FastAPI!"
print(my_string_variable)
print(type(my_string_variable))

# Redefinimos la variable con type hints y no guarda el tipo string, esto es porque Python no es un lenguaje de tipado fuerte
my_string_variable = 5
print(my_string_variable)
print(type(my_string_variable))

# Se recomienda tipar para FastAPI, ya que nos ayuda a tener un código más legible y mantenible, además de que nos permite aprovechar las ventajas de la autocompletación y la validación de tipos en tiempo de desarrollo.
my_string_variable: str = "Hello, FastAPI!"
my_string_variable.count # Esto nos permite ver los métodos disponibles para el tipo string, como count, upper, lower, etc.

