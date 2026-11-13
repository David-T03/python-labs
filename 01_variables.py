#Variables

my_string_variable = "My String Variable"
print(my_string_variable)

my_int_variable = 10
print(my_int_variable)

my_float_variable = 10.5
print(my_float_variable)

my_bool_variable = True
print(my_bool_variable)

#Concatenación de variables
print(my_string_variable, my_int_variable, my_float_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable) # Concatenación de variables con texto

#Variable len
print(len(my_string_variable)) # Longitud de la variable

#Variable en una línea
name, surname, alias, age = "David", "Marín", "Tombo", 25
print("Me llamo:", name, surname, ",mi edad es:", age, "y mi alias es:",alias)

#Variable input
name = input("¿Cuál es tu nombre?: ")
age = input("¿Cuál es tu edad?: ")
print("Hola", name, ",tienes", age, "años")

