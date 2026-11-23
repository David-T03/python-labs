### Loops ###

# While

my_condition = 0
while my_condition < 10: # Mientras my_condition sea menor que 10 se ejecutará el bucle infiitamente
    print("Se cumple la condición")
    my_condition += 1 # Se le suma 1 a my_condition
    print("El valor de my_condition es: ", my_condition)
else: # Es opcional, se ejecuta cuando la condición del while es False
    print("Se ha salido del bucle while")

print("La ejecución del programa continúa")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se ha alcanzado el valor de 15, se sale del bucle")
        break # Se sale del bucle while
    print("El valor de my_condition es: ", my_condition)

print("La ejecución del programa continúa")

# For

my_list = [1, 2, 3, 4, 5] # Funciona con listas, tuplas, diccionarios, sets y strings
for element in my_list: # Se recorre la lista y se asigna cada elemento a la variable element
    print("El valor del elemento es: ", element)

for element in my_list:
    if element == 3:
        print("Se ha alcanzado el valor de 3, se sale del bucle")
        break # Se sale del bucle for
    print("El valor del elemento es: ", element)

for element in my_list:
    if element == 3:
        print("Se ha alcanzado el valor de 3, se salta a la siguiente iteración")
        continue # Se salta a la siguiente iteración del bucle for
    print("El valor del elemento es: ", element)