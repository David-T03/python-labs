### Tuplas ###

my_tuple = tuple() #Define una tupla vacía
my_other_tuple = () #Define otra tupla vacía

my_tuple = (35, 1.76, "Alonso", "Marín") #Define una tupla con varios elementos
my_other_tuple = (25, 1.74, "David", "Ruiz") #Define otra tupla con varios elementos
print(my_tuple) #Imprime la tupla completa
print(len(my_tuple)) #Imprime la longitud de la tupla
print(type(my_tuple)) #Imprime el tipo de dato de la tupla

print(my_tuple[0]) #Imprime el primer elemento de la tupla
print(my_tuple[-1]) #Imprime el último elemento de la tupla

my_tuple.count("Alonso") #Cuenta cuántas veces aparece el elemento "Alonso" en la tupla
my_tuple.index("Marín") #Devuelve el índice del elemento "Marín" en la tupla
print(my_tuple.count("Alonso")) #Imprime cuántas veces aparece "Alonso"
print(my_tuple.index("Marín")) #Imprime el índice de "Marín"


#my_tuple[1] = 1.80 #Esto generará un error porque las tuplas son inmutables

print(my_tuple + my_other_tuple) #Concatena dos tuplas
my_sum_tuple = my_tuple + my_other_tuple #Concatena dos tuplas y las asigna a una nueva variable
print(my_sum_tuple) #Imprime la tupla resultante de la concatenación
print(my_sum_tuple[3:4]) #Imprime los elementos de la tupla resultante desde el índice 3 hasta el final

del my_sum_tuple #Elimina la tupla resultante de la concatenación
#print(my_sum_tuple) #Esto generará un error porque la tupla ha sido eliminada