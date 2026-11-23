### Clases ###

class Person: #Los nombres de las clases se escriben en mayúscula
    def __init__(self, name, age): #El método init es el constructor de la clase
        self.name = name #Atributos de la clase
        self.age = age

my_person = Person("David", 25) #Instancia de la clase Person
print(my_person.name) #Imprime el nombre de la persona
print(my_person.age) #Imprime la edad de la persona


class Person2:
    def __init__(self, name, surname):
        self.full_name = f"{name} {surname}" #Atributo de la clase que combina el nombre y el apellido
        self.__name = name #Atributo privado de la clase que almacena el nombre

    def get_name(self):
        return self.__name #Método que devuelve el valor del atributo privado __name

    def walk(self):
        print(f"{self.full_name} está caminando") #Método de la clase que imprime un mensaje indicando que la persona está caminando

my_person2 = Person2("David", "Ruiz") #Instancia de la clase Person2
print(my_person2.get_name()) #Imprime el nombre de la persona usando el método get_name
print(my_person2.full_name) #Imprime el nombre completo de la persona
my_person2.walk() #Llama al método walk para imprimir el mensaje

class Estudiante(Person2): #La clase Estudiante hereda de la clase Person2
    def __init__(self, name, surname, student_id):
        super().__init__(name, surname) #Llama al constructor de la clase padre (Person2)
        self.student_id = student_id #Atributo de la clase Estudiante

    def study(self):
        print(f"{self.full_name} está estudiando") #Método de la clase Estudiante que imprime un mensaje indicando que el estudiante está estudiando

my_student = Estudiante("David", "Ruiz", "12345") #Instancia de la clase Estudiante
print(my_student.get_name()) #Imprime el nombre del estudiante usando el método get_name heredado de la clase Person2
print(my_student.full_name) #Imprime el nombre completo del estudiante
print(my_student.student_id) #Imprime el ID del estudiante
my_student.study() #Llama al método study para imprimir el mensaje