### Lists ###

my_list = list()  # Crea una lista vacía
my_other_list = []  # Crea una lista vacía
my_other_list = [1, 2, 3, 4, 5]  # Crea una lista con elementos

print(len(my_other_list))  # Imprime la longitud de la lista
print(my_other_list)  # Imprime la lista

my_other_list = ["David", 25, 1.75, "Python"]  # Crea una lista con elementos de diferentes tipos
print(my_other_list)  # Imprime la lista
print(type(my_other_list))  # Imprime el tipo de la lista
print(my_other_list[0])  # Imprime el primer elemento de la lista
print(my_other_list[-1])  # Imprime el último elemento de la lista
print(my_other_list.count(25))  # Cuenta cuántas veces aparece 25 en la lista

name, age, height, language = my_other_list  # Desempaqueta la lista en variables
print(name)  # Imprime la variable name
print(age)  # Imprime la variable age
print(height)  # Imprime la variable height
print(language)  # Imprime la variable language

my_other_list.append("28")  # Agrega un nuevo elemento al final de la lista
print(my_other_list)  # Imprime la lista

my_other_list.insert(1, "Rojo")  # Inserta un nuevo elemento en la posición 1 de la lista
print(my_other_list)  # Imprime la lista

my_other_list.remove("Rojo")  # Elimina el elemento "Rojo" de la lista
print(my_other_list)  # Imprime la lista

my_other_list.pop(2)  # Elimina el elemento en la posición 2 de la lista
print(my_other_list)  # Imprime la lista

my_other_list.insert(1, "85")  # Inserta un nuevo elemento en la posición 1 de la lista
print(my_other_list)  # Imprime la lista

my_other_list.insert(1, "878")  # Inserta un nuevo elemento en la posición 1 de la lista
print(my_other_list)  # Imprime la lista

my_pop_element = my_other_list.pop(1)  # Elimina el último elemento de la lista y lo guarda en una variable
print(my_pop_element)  # Imprime el elemento eliminado

del my_other_list[0]  # Elimina el primer elemento de la l ista
print(my_other_list)  # Imprime la lista

my_new_list = my_other_list.copy()  # Crea una copia de la lista
print(my_new_list)  # Imprime la copia de la lista

del my_new_list[1]  # Elimina el primer elemento de la copia de la lista

my_other_list.clear()  # Elimina todos los elementos de la lista
print(my_other_list)  # Imprime la lista

my_new_list.reverse()  # Invierte el orden de los elementos de la lista
print(my_new_list)  # Imprime la lista invertida

my_new_list.sort()  # Ordena los elementos de la lista
print(my_new_list)  # Imprime la lista ordenada