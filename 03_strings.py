### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))


print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

# Formateo de Strings #
name, surname, age = "David", "Marín", 25
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))


# Desempaquetado de caracteres #
language = "Python"
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# División de Strings #
language_slice = language[1:3]
print(language_slice)


language_slice = language[1:]
print(language_slice)

# Reverse de Strings #
reverse_language = language[::-1]
print(reverse_language)


# Funciones de Strings #
print(language.capitalize()) # Convierte el primer carácter en mayúscula
print(language.upper()) # Convierte todos los caracteres en mayúsculas
print(language.lower()) # Convierte todos los caracteres en minúsculas
print(language.count("t")) # Cuenta cuántas veces aparece un carácter en el String
print(language.isnumeric()) # Comprueba si el String es numérico
print("1".isnumeric()) # Comprueba si el String es numérico
print(language.startswith("Py")) # Comprueba si el String empieza con un carácter específico
print(language.endswith("on")) # Comprueba si el String termina con un carácter específico