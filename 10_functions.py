### Funciones ###

# Esta función no recibe parámetros ni devuelve un valor.
def my_function():
    print("Esta es una función simple.")


# Podemos llamar una misma función varias veces.
my_function ()
my_function ()
my_function ()

# Esta función recibe dos valores y muestra su suma.
def sum_two_values(first_number, second_number):
    print(first_number + second_number)

# Los números se pueden sumar normalmente.
sum_two_values (5, 7)
sum_two_values (87, 87)
# Los textos se unen con el operador + (concatenación).
sum_two_values ("5", "7")
sum_two_values ("Hola", "Pura vida")
# También se pueden sumar números decimales.
sum_two_values (4.5, 4.2)

# Esta función calcula el resultado y lo devuelve con return.
def sum_two_values_with_return (first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

# Guardamos el valor devuelto en una variable.
my_result = sum_two_values_with_return(10, 5)
print(my_result)


# Esta función recibe dos parámetros.
def print_name(name, surname):
    print(f"{name} {surname}")

# Los argumentos también pueden indicarse por nombre.
print_name(surname = "Marín", name = "David") 