### Diccionario ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre" : "David", "Apellido" : "Marín", "Edad" : 25, 1: "Python"}
print(my_other_dict)

my_dict = {
    
    "Nombre" : "David",
    "Apellido" : "Marín",
    "Edad" : 25,
    "Lenguajes" : {"Python", "Swift", "Kotlin"},
    1: 1.77
}
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))


print(my_dict["Nombre"])

# cambiar el valor de un elemento del diccionario #
my_dict["Nombre"] = "Alonso"
print(my_dict["Nombre"])

print(my_dict[1])
print(my_dict["Lenguajes"])

# Asi se agrega un nuevo elemento al diccionario #
my_dict["Calle"] = "Calle falsa 123"
print(my_dict)


# Eliminar un elemento del diccionario #
del my_dict["Calle"]
print(my_dict)

# Comprobar si un elemento se encuentra en el diccionario #
print("Marín" in my_dict)
print("Nombre" in my_dict)

# Algunos métodos de los diccionarios #
print(my_dict.items()) # Devuelve una lista de tuplas con las claves y valores
print(my_dict.keys()) # Devuelve una lista con las claves
print(my_dict.values()) # Devuelve una lista con los valores

my_new_dict = my_other_dict.fromkeys(("Nombre", 1)) # Crea un nuevo diccionario con las claves especificadas y valores por defecto
print(my_new_dict)