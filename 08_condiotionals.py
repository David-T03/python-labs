### Conditionals ###

my_condition = False

if my_condition: # Es lo mismo que if my_condition == True
    print("Se cumple la condición")

my_condition = 5*5 # Se le da valor a my condition
if my_condition == 10: # Se comprueba si es True
    print("Se cumple la segunda condición")

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25: # Solo se ejecuta si la condición anterior es False
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")

print("Fin del programa")

