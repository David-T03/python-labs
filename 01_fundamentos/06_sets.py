### Sets ###

my_set = set() #Define un set vacío
my_other_set = {} #Define un diccionario vacío, no un set
print(type(my_set)) #Imprime el tipo de dato del set
print(type(my_other_set)) #Imprime el tipo de dato del diccionario

my_set = {35, 1.76, "Alonso", "Marín"} #Define un set con varios elementos
my_other_set = {25, 1.74, "David", "Ruiz"} #Define otro set con varios elementos
print(my_set) #Imprime el set completo
print(type(my_other_set)) #Imprime el tipo de dato del set

print(len(my_set)) #Imprime la longitud del set

my_set.add("Costa Rica") #Agrega un elemento al set
print(my_set) #Imprime el set con el nuevo elemento agregado
my_set.add("Costa Rica") #Intenta agregar un elemento que ya existe en el set
print(my_set) #Imprime el set, el elemento duplicado no se agrega

print("Alonso" in my_set) #Imprime True si el elemento "Alonso" está en el set, de lo contrario imprime False
print("España" in my_set) #Imprime True si el elemento "España" está en el set, de lo contrario imprime False   

my_set.remove("Alonso") #Elimina el elemento "Alonso" del set
print(my_set) #Imprime el set sin el elemento eliminado


my_set.clear() #Elimina todos los elementos del set
print(my_set) #Imprime el set vacío

my_new_set = my_set.union(my_other_set) #Une dos sets y los asigna a una nueva variable
print(my_new_set.union(my_new_set).union(my_set).union({"Colombia", "Chile", "Ruiz"})) #Imprime el set resultante de la unión de los dos sets

print(my_new_set.difference(my_set)) #Imprime los elementos que están en my_new_set pero no en my_set
print(my_new_set.intersection(my_set)) #Imprime los elementos que están en ambos sets