# 🐍 python-labs

Un repositorio práctico donde se documenta y aprende lo básico de Python paso a paso, dividido por módulos temáticos.

---

## 📂 Índice de Contenido

1. [`00_hello.py` - Introducción y Primeros Pasos](#00_hellopy---introducción-y-primeros-pasos)
2. [`01_variables.py` - Variables y Funciones Integradas](#01_variablespy---variables-y-funciones-integradas)
3. [`02_operadores.py` - Operadores en Python](#02_operadorespy---operadores-en-python)
4. [`03_strings.py` - Cadenas de Texto (Strings)](#03_stringspy---cadenas-de-texto-strings)
5. [`04_list.py` - Listas (Lists)](#04_listpy---listas-lists)
6. [`05_tuplas.py` - Tuplas (Tuples)](#05_tuplapy---tuplas-tuples)
7. [`06_sets.py` - Conjuntos (Sets)](#06_setspy---conjuntos-sets)
8. [`07_dicts.py` - Diccionarios (Dictionaries)](#07_dictspy---diccionarios-dictionaries)
9. [`08_conditionals.py` - Condicionales (Conditionals)](#08_conditionalspy---condicionales-conditionals)
10. [`09_loops.py` - Bucles o Ciclos (Loops)](#09_loopspy---bucles-o-ciclos-loops)
11. [`10_functions.py` - Funciones (Functions)](#10_functionspy---funciones-functions)
12. [`11_classes.py` - Clases y Programación Orientada a Objetos (POO)](#11_classespy---clases-y-programación-orientada-a-objetos-poo)
13. [`12_exceptions.py` - Manejo de Excepciones (Exception Handling)](#12_exceptionspy---manejo-de-excepciones-exception-handling)
14. [`13_modules.py` - Módulos (Modules)](#13_modulespy---módulos-modules)
15. [📚 Material Adicional y Créditos](#-material-adicional-y-créditos)

---

## `00_hello.py` - Introducción y Primeros Pasos

Primer acercamiento a la sintaxis de Python, salida por consola, comentarios y verificación de tipos de datos primitivos.

* **Salida estándar:** Uso de `print()` para mostrar mensajes y resultados en consola.
* **Comentarios:**
  * `#` para comentarios de una sola línea.
  * `""" """` o `''' '''` para comentarios multilínea o *docstrings*.
* **Tipos de datos básicos:** `int` (enteros), `float` (decimales), `complex` (complejos), `str` (cadenas de texto), `bool` (booleanos) y colecciones iniciales (`list`, `tuple`, `set`, `dict`).
* **Inspección de tipos:** Uso de `type()` para comprobar qué tipo de dato almacena un valor o variable.

---

## `01_variables.py` - Variables y Funciones Integradas

### Convenciones para Nombres de Variables en Python

En Python las variables son de tipado dinámico y no requieren declaración previa. Se recomienda seguir el estándar **PEP 8**:

* Nombres de una sola palabra en minúsculas como `firstname`, `lastname`, `age`, `country` y `city`.
* Nombres compuestos separados por guiones bajos (*snake_case*) como `first_name`, `last_name`, `capital_city` y `birth_year`.
* Uso de números integrados o al final como `year2021`, `year_2021`, `current_year_2021`, `num1` y `num2`.
* Uso de un guion bajo inicial (`_if`) para evitar conflictos si se desea utilizar una palabra reservada como variable.
* **Reglas estrictas:** No pueden empezar con un número, ni contener espacios o caracteres especiales (`$`, `-`, `@`, etc.).

### Funciones Integradas (Built-in) en Python - Cheat Sheet

| Función | Descripción | Ejemplo Práctico |
|---------|-------------|------------------|
| `abs()` | Devuelve el valor absoluto de un número. | `abs(-5)` devuelve `5` |
| `all()` | Devuelve `True` si todos los elementos de un iterable son verdaderos. | `all([True, True, False])` devuelve `False` |
| `any()` | Devuelve `True` si algún elemento de un iterable es verdadero. | `any([False, True, False])` devuelve `True` |
| `ascii()` | Devuelve una cadena con una representación imprimible de un objeto. | `ascii('ñ')` devuelve `'\xf1'` |
| `bin()` | Convierte un número entero a una cadena binaria. | `bin(3)` devuelve `'0b11'` |
| `bool()` | Convierte un valor a booleano (`True` o `False`). | `bool(1)` devuelve `True` |
| `breakpoint()` | Entra al depurador (debugger) de Python en esa línea. | `breakpoint()` |
| `bytearray()` | Devuelve un arreglo de bytes mutable. | `bytearray([50, 100])` |
| `bytes()` | Devuelve un objeto de bytes inmutable. | `bytes([50, 100])` |
| `callable()` | Comprueba si el objeto se puede llamar (como una función). | `callable(print)` devuelve `True` |
| `chr()` | Devuelve el carácter que representa un código Unicode. | `chr(97)` devuelve `'a'` |
| `classmethod()` | Decorador para convertir un método en un método de clase. | `@classmethod` |
| `compile()` | Compila código fuente en un objeto de código ejecutable. | `compile('print(1)', '', 'exec')` |
| `complex()` | Crea un número complejo. | `complex(1, 2)` devuelve `(1+2j)` |
| `delattr()` | Elimina un atributo de un objeto. | `delattr(obj, 'nombre_atributo')` |
| `dict()` | Crea un nuevo diccionario. | `dict(a=1, b=2)` devuelve `{'a': 1, 'b': 2}` |
| `dir()` | Devuelve una lista de atributos y métodos válidos de un objeto. | `dir(list)` |
| `divmod()` | Devuelve el cociente y el residuo de una división. | `divmod(10, 3)` devuelve `(3, 1)` |
| `enumerate()` | Agrega un contador a un iterable y lo devuelve como objeto enumerado. | `list(enumerate(['a', 'b']))` devuelve `[(0, 'a'), (1, 'b')]` |
| `eval()` | Evalúa y ejecuta una expresión Python desde una cadena de texto. | `eval('1 + 1')` devuelve `2` |
| `exec()` | Ejecuta código Python dinámico (múltiples líneas). | `exec('a = 2\nprint(a)')` |
| `filter()` | Filtra elementos de un iterable usando una función que devuelve booleano. | `list(filter(None, [0, 1, False, 2]))` devuelve `[1, 2]` |
| `float()` | Convierte un número o cadena a un número de punto flotante (decimal). | `float("3.14")` devuelve `3.14` |
| `format()` | Formatea un valor según una especificación. | `format(0.5, '%')` devuelve `'50.000000%'` |
| `frozenset()` | Crea un objeto set inmutable. | `frozenset([1, 2, 2])` devuelve `frozenset({1, 2})` |
| `getattr()` | Obtiene el valor de un atributo de un objeto. | `getattr(obj, 'atributo')` |
| `globals()` | Devuelve un diccionario con la tabla de variables globales actuales. | `globals()` |
| `hasattr()` | Comprueba si un objeto tiene un atributo específico. | `hasattr(obj, 'atributo')` devuelve `True` o `False` |
| `hash()` | Devuelve el valor hash de un objeto (si lo tiene). | `hash("hola")` |
| `help()` | Abre el sistema de ayuda integrado para módulos o funciones. | `help(str)` |
| `hex()` | Convierte un número entero a una cadena hexadecimal. | `hex(255)` devuelve `'0xff'` |
| `id()` | Devuelve la identidad única (dirección de memoria) de un objeto. | `id(obj)` |
| `input()` | Pausa la ejecución y lee una línea de entrada del usuario. | `nombre = input("Nombre: ")` |
| `int()` | Convierte un número o cadena a un número entero. | `int("10")` devuelve `10` |
| `isinstance()` | Comprueba si un objeto es una instancia de una clase dada. | `isinstance(5, int)` devuelve `True` |
| `issubclass()` | Comprueba si una clase es subclase de otra. | `issubclass(bool, int)` devuelve `True` |
| `iter()` | Devuelve un iterador para un objeto. | `iter([1, 2, 3])` |
| `len()` | Devuelve la longitud (cantidad de elementos) de un objeto. | `len("hola")` devuelve `4` |
| `list()` | Crea una nueva lista. | `list((1, 2))` devuelve `[1, 2]` |
| `locals()` | Devuelve un diccionario con las variables locales actuales. | `locals()` |
| `map()` | Aplica una función a todos los elementos de un iterable. | `list(map(abs, [-1, -2]))` devuelve `[1, 2]` |
| `max()` | Devuelve el elemento de mayor valor en un iterable. | `max(1, 5, 2)` devuelve `5` |
| `memoryview()` | Devuelve un objeto de vista de memoria de un argumento. | `memoryview(b'ab')` |
| `min()` | Devuelve el elemento de menor valor en un iterable. | `min(1, 5, 2)` devuelve `1` |
| `next()` | Recupera el siguiente elemento de un iterador. | `next(mi_iterador)` |
| `object()` | Devuelve un nuevo objeto base sin características. | `object()` |
| `oct()` | Convierte un número entero a una cadena octal. | `oct(8)` devuelve `'0o10'` |
| `open()` | Abre un archivo y devuelve el flujo de datos (file object). | `open("archivo.txt", "r")` |
| `ord()` | Devuelve el número Unicode que representa un carácter. | `ord('a')` devuelve `97` |
| `pow()` | Devuelve la base elevada a un exponente. | `pow(2, 3)` devuelve `8` |
| `print()` | Imprime objetos en la salida estándar (consola). | `print("Hola mundo")` |
| `property()` | Devuelve un atributo de propiedad (útil en clases). | `property(get_x, set_x)` |
| `range()` | Genera una secuencia inmutable de números. | `list(range(3))` devuelve `[0, 1, 2]` |
| `repr()` | Devuelve una representación en cadena formal de un objeto. | `repr("a")` devuelve `"'a'"` |
| `reversed()` | Devuelve un iterador inverso de una secuencia. | `list(reversed([1, 2, 3]))` devuelve `[3, 2, 1]` |
| `round()` | Redondea un número flotante a cierta cantidad de decimales. | `round(3.14159, 2)` devuelve `3.14` |
| `set()` | Crea un nuevo conjunto (colección sin elementos duplicados). | `set([1, 2, 2, 3])` devuelve `{1, 2, 3}` |
| `setattr()` | Establece el valor del atributo de un objeto. | `setattr(obj, 'atributo', 5)` |
| `slice()` | Devuelve un objeto de porción para extraer partes de iterables. | `slice(1, 5, 2)` |
| `sorted()` | Devuelve una nueva lista ordenada a partir del iterable. | `sorted([3, 1, 2])` devuelve `[1, 2, 3]` |
| `staticmethod()` | Decorador para convertir un método en un método estático. | `@staticmethod` |
| `str()` | Convierte un valor a una cadena de texto (string). | `str(50)` devuelve `'50'` |
| `sum()` | Suma todos los elementos numéricos de un iterable. | `sum([1, 2, 3])` devuelve `6` |
| `super()` | Devuelve un objeto proxy que delega llamadas a una clase padre. | `super().__init__()` |
| `tuple()` | Crea una tupla inmutable. | `tuple([1, 2])` devuelve `(1, 2)` |
| `type()` | Devuelve el tipo de dato de un objeto. | `type(5)` devuelve `<class 'int'>` |
| `vars()` | Devuelve el atributo `__dict__` (diccionario) de un objeto. | `vars(obj)` |
| `zip()` | Itera sobre varios iterables agrupando sus elementos en paralelo. | `list(zip([1, 2], ['a', 'b']))` devuelve `[(1, 'a'), (2, 'b')]` |
| `__import__()` | Función interna invocada por la instrucción `import`. | `__import__('math')` |

---

## `02_operadores.py` - Operadores en Python

### Operadores Aritméticos

Se utilizan con valores numéricos para realizar operaciones matemáticas comunes.

| Operador | Nombre | Descripción / Ejemplo |
| :--- | :--- | :--- |
| `+` | Suma | Suma dos valores (ej. `5 + 3` da `8`) |
| `-` | Resta | Resta el segundo valor del primero (ej. `5 - 3` da `2`) |
| `*` | Multiplicación | Multiplica ambos valores (ej. `5 * 3` da `15`) |
| `/` | División | Divide el primer valor entre el segundo, devolviendo un decimal (ej. `5 / 2` da `2.5`) |
| `%` | Módulo | Devuelve el residuo o sobrante de una división (ej. `5 % 2` da `1`) |
| `**` | Exponenciación | Eleva un número a la potencia de otro (ej. `2 ** 3` da `8`) |
| `//` | División entera | Divide y redondea el resultado hacia abajo al número entero más cercano (ej. `5 // 2` da `2`) |

### Operadores de Asignación

Se utilizan para asignar valores a las variables combinándolos con operaciones matemáticas o lógicas.

| Operador | Ejemplo | Equivalente a |
| :--- | :--- | :--- |
| `=` | `x = 5` | `x = 5` |
| `+=` | `x += 3` | `x = x + 3` |
| `-=` | `x -= 3` | `x = x - 3` |
| `*=` | `x *= 3` | `x = x * 3` |
| `/=` | `x /= 3` | `x = x / 3` |
| `%=` | `x %= 3` | `x = x % 3` |
| `//=` | `x //= 3` | `x = x // 3` |
| `**=` | `x **= 3` | `x = x ** 3` |
| `&=` | `x &= 3` | `x = x & 3` |
| `\|=` | `x \|= 3` | `x = x \| 3` |
| `^=` | `x ^= 3` | `x = x ^ 3` |
| `>>=` | `x >>= 3` | `x = x >> 3` |
| `<<=` | `x <<= 3` | `x = x << 3` |

### Operadores de Comparación

Se utilizan para comparar dos valores y devuelven un valor booleano (`True` o `False`).

| Operador | Nombre | Ejemplo |
| :--- | :--- | :--- |
| `==` | Igual a | `x == y` |
| `!=` | Distinto de (No igual) | `x != y` |
| `>` | Mayor que | `x > y` |
| `<` | Menor que | `x < y` |
| `>=` | Mayor o igual que | `x >= y` |
| `<=` | Menor o igual que | `x <= y` |

### Operadores Lógicos

Se utilizan para combinar declaraciones condicionales.

| Operador | Descripción | Ejemplo |
| :--- | :--- | :--- |
| `and` | Devuelve `True` si ambas afirmaciones son verdaderas | `x < 5 and x < 10` |
| `or` | Devuelve `True` si al menos una de las afirmaciones es verdadera | `x < 5 or x < 4` |
| `not` | Invierte el resultado; devuelve `False` si el resultado es verdadero | `not(x < 5 and x < 10)` |

---

## `03_strings.py` - Cadenas de Texto (Strings)

Los *strings* en Python son secuencias **inmutables** de caracteres delimitadas por comillas simples (`' '`), dobles (`" "`) o triples (`''' '''`).

### Conceptos Clave
* **Secuencias de escape:** `\n` (salto de línea), `\t` (tabulación), `\\` (barra invertida), `\'` (comilla simple), `\"` (comilla doble).
* **Formateo de cadenas:**
  * **f-strings (Recomendado):** `f"Hola, {nombre}. Tienes {edad} años."`
  * **`.format()`:** `"Hola, {}. Tienes {} años.".format(nombre, edad)`
  * **Operador `%` (clásico):** `"Hola, %s. Tienes %d años." % (nombre, edad)`
* **Desempaquetado e Indexación:**
  * Índices positivos desde `0` (izquierda a derecha) y negativos desde `-1` (derecha a izquierda).
  * **Slicing (rebanado):** `texto[inicio:fin:paso]` (ej. `texto[::-1]` invierte la cadena).

### Métodos más utilizados en Strings

| Método | Descripción | Ejemplo |
| :--- | :--- | :--- |
| `.capitalize()` | Convierte el primer carácter en mayúscula. | `'python'.capitalize()` -> `'Python'` |
| `.upper()` / `.lower()` | Convierte toda la cadena a mayúsculas o minúsculas. | `'Hola'.upper()` -> `'HOLA'` |
| `.count(sub)` | Cuenta cuántas veces aparece una subcadena. | `'banana'.count('a')` -> `3` |
| `.find(sub)` | Devuelve el índice de la primera aparición (`-1` si no existe). | `'python'.find('th')` -> `2` |
| `.replace(old, new)` | Reemplaza una subcadena por otra. | `'hola mundo'.replace('mundo', 'Python')` |
| `.split(sep)` | Divide la cadena en una lista usando un separador. | `'a,b,c'.split(',')` -> `['a', 'b', 'c']` |
| `.strip()` | Elimina espacios en blanco (o caracteres) al inicio y al final. | `'  hola  '.strip()` -> `'hola'` |
| `.startswith()` / `.endswith()` | Verifica si la cadena empieza o termina con un texto dado. | `'archivo.py'.endswith('.py')` -> `True` |
| `.isnumeric()` / `.isalpha()` | Comprueba si todos los caracteres son numéricos o alfabéticos. | `'123'.isnumeric()` -> `True` |

---

## `04_list.py` - Listas (Lists)

Una lista es una colección **ordenada**, **mutable** (se puede modificar después de crearse) y que **permite elementos duplicados** de distintos tipos de datos. Se definen usando corchetes `[]` o el constructor `list()`.

### Operaciones Comunes
* **Acceso y modificación:** `mi_lista[0] = "nuevo_valor"`
* **Slicing:** `mi_lista[1:4]` extrae una sublista desde el índice 1 hasta el 3.
* **Desempaquetado:** `primero, segundo, *resto = [1, 2, 3, 4, 5]`
* **Verificación:** `'elemento' in mi_lista` devuelve `True` o `False`.
* **Concatenación:** `lista_total = lista_1 + lista_2`

### Métodos principales de Listas

| Método | Descripción | Ejemplo |
| :--- | :--- | :--- |
| `.append(x)` | Agrega un elemento al final de la lista. | `nums.append(4)` |
| `.insert(i, x)` | Inserta un elemento en una posición específica `i`. | `nums.insert(1, 'nuevo')` |
| `.extend(iterable)` | Agrega todos los elementos de otro iterable al final. | `nums.extend([5, 6])` |
| `.remove(x)` | Elimina la primera aparición del valor `x`. | `nums.remove('nuevo')` |
| `.pop(i)` | Elimina y devuelve el elemento en el índice `i` (por defecto el último). | `ultimo = nums.pop()` |
| `.clear()` | Vacía todos los elementos de la lista. | `nums.clear()` |
| `.index(x)` | Devuelve el índice de la primera aparición de `x`. | `nums.index(4)` |
| `.count(x)` | Cuenta cuántas veces aparece `x` en la lista. | `nums.count(2)` |
| `.sort(reverse=False)` | Ordena la lista original (*in-place*) de forma ascendente o descendente. | `nums.sort()` |
| `.reverse()` | Invierte el orden de los elementos de la lista original. | `nums.reverse()` |
| `.copy()` | Devuelve una copia superficial (*shallow copy*) de la lista. | `copia = nums.copy()` |

## `05_tuplas.py` - Tuplas (Tuples)

Una **tupla** es una colección **ordenada** e **inmutable** de elementos que permite valores duplicados y de distintos tipos de datos (`int`, `float`, `str`, etc.). Se definen utilizando paréntesis `()` o el constructor `tuple()`.

### ¿Cuándo y por qué usar una Tupla en lugar de una Lista?
* **Seguridad e integridad de datos:** Al ser inmutables, garantizan que los datos no sean modificados accidentalmente en otra parte del programa (por ejemplo: coordenadas, fechas, configuraciones fijas o registros de base de datos).
* **Rendimiento:** Ocupan menos espacio en memoria y son ligeramente más rápidas de recorrer que las listas.
* **Uso como claves:** A diferencia de las listas, las tuplas pueden utilizarse como claves (*keys*) dentro de un diccionario si contienen elementos inmutables.

### Conceptos y Operaciones Clave

* **Definición y tipos:**
  * Vacías: `my_tuple = tuple()` o `my_other_tuple = ()`.
  * Con datos: `my_tuple = (35, 1.76, "Alonso", "Marín")`.
  * **Tupla de un solo elemento:** Requiere una coma al final (`(35,)`), de lo contrario Python lo interpreta como un entero o cadena normal.
  * **Empaquetado implícito:** Python permite crear tuplas sin paréntesis separando valores por comas: `datos = 35, 1.76, "Alonso"`.
* **Inmutabilidad estricta:** Intentar reasignar un valor directamente (ej. `my_tuple[1] = 1.80`) arroja un `TypeError`. Si necesitas modificarla, primero debes convertirla a lista con `list()`, cambiar el dato y volverla a convertir con `tuple()`.
* **Acceso y Slicing (rebanado):**
  * Índices positivos desde `0` (`my_tuple[0]` -> `35`) y negativos desde `-1` (`my_tuple[-1]` -> `"Marín"`).
  * Subtuplas mediante rangos: `my_sum_tuple[3:4]` extrae una nueva tupla con el elemento en el índice `3` (el límite superior es exclusivo; para ir hasta el final se usa `my_sum_tuple[3:]`).
* **Concatenación y eliminación:**
  * Se pueden sumar dos tuplas para generar una nueva sin alterar las originales: `my_sum_tuple = my_tuple + my_other_tuple`.
  * Al no poder borrar elementos individuales, `del my_sum_tuple` elimina por completo la variable de la memoria.
* **Desempaquetado (Unpacking):** Permite asignar cada elemento de la tupla a variables individuales en una sola línea:
  ```python
  edad, estatura, nombre, apellido = my_tuple

  ### Métodos propios de las Tuplas

Debido a su inmutabilidad, las tuplas únicamente poseen **dos métodos nativos**:

| Método | Descripción | Ejemplo |
| :--- | :--- | :--- |
| `.count(x)` | Devuelve cuántas veces aparece el elemento `x` dentro de la tupla. | `my_tuple.count("Alonso")` -> `1` |
| `.index(x)` | Devuelve el índice de la primera aparición de `x` (lanza `ValueError` si no existe). | `my_tuple.index("Marín")` -> `3` |

### Funciones integradas (Built-in) compatibles con Tuplas

Aunque no son métodos propios del objeto `tuple`, estas funciones de Python se utilizan constantemente para operar sobre ellas:

| Función | Descripción | Ejemplo |
| :--- | :--- | :--- |
| `len(tupla)` | Devuelve la cantidad total de elementos en la tupla. | `len((10, 20, 30))` -> `3` |
| `max(tupla)` | Devuelve el elemento de mayor valor (requiere elementos comparables entre sí). | `max((4, 9, 1))` -> `9` |
| `min(tupla)` | Devuelve el elemento de menor valor. | `min((4, 9, 1))` -> `1` |
| `sum(tupla)` | Suma todos los elementos numéricos de la tupla. | `sum((10, 20, 30))` -> `60` |
| `sorted(tupla)` | Devuelve una **nueva lista** con los elementos ordenados (no modifica la tupla). | `sorted((3, 1, 2))` -> `[1, 2, 3]` |
| `tuple(iterable)` | Convierte otro iterable (lista, string, set) en una tupla. | `tuple([1, 2, 3])` -> `(1, 2, 3)` |
| `any(tupla)` | Devuelve `True` si al menos un elemento de la tupla es verdadero. | `any((0, False, 5))` -> `True` |
| `all(tupla)` | Devuelve `True` si todos los elementos de la tupla son verdaderos. | `all((1, True, "a"))` -> `True` |
| `enumerate(tupla)` | Devuelve un iterador de tuplas con índice y valor `(índice, elemento)`. | `list(enumerate(('a', 'b')))` -> `[(0, 'a'), (1, 'b')]` |

---

## `06_sets.py` - Conjuntos (Sets)

Un **set** (conjunto) es una colección **no ordenada**, **no indexada**, **mutable** y que **no permite elementos duplicados**. Internamente utilizan tablas *hash*, lo que los hace extremadamente rápidos para verificar si un elemento existe dentro de ellos.

### ¿Cuándo y por qué usar un Set?
* **Eliminar duplicados automáticamente:** Si agregas un elemento repetido (como hacer `.add("Costa Rica")` dos veces), Python simplemente lo ignora. También es ideal para limpiar listas convirtiéndolas con `set(mi_lista)`.
* **Búsquedas ultrarrápidas:** Comprobar pertenencia con el operador `in` (ej. `"Alonso" in my_set`) es mucho más eficiente en un `set` que en una `list` o `tuple`.
* **Operaciones matemáticas de conjuntos:** Permiten calcular uniones, intersecciones y diferencias entre grupos de datos de forma nativa.

### Conceptos y Reglas Clave

* **Trampa al crear un set vacío (`{}` vs `set()`):**
  * `my_set = set()` crea un **set vacío** (`<class 'set'>`).
  * `my_other_set = {}` crea un **diccionario vacío** (`<class 'dict'>`), aunque al asignarle elementos sin clave-valor (`{25, 1.74, "David", "Ruiz"}`) Python sí lo reconoce como `set`.
* **Sin orden ni índices:** Al no mantener un orden fijo, el resultado de `print(my_set)` puede variar en cada ejecución y **no soporta indexación ni slicing** (`my_set[0]` lanzará un `TypeError`).
* **Elementos inmutables:** Un set puede modificarse (agregar o quitar elementos), pero los elementos guardados dentro de él deben ser inmutables (*hashables*), como números, strings o tuplas. No puede contener listas ni otros sets.
* **Comprobación de existencia:** Se utiliza `elemento in my_set` o `elemento not in my_set` para obtener un booleano (`True` o `False`).

### Métodos principales y Operaciones de Conjuntos

| Método / Operador | Descripción | Ejemplo |
| :--- | :--- | :--- |
| `.add(x)` | Agrega un único elemento `x` al set. Si ya existe, no hace nada. | `my_set.add("Costa Rica")` |
| `.update(iterable)` | Agrega múltiples elementos de una lista, tupla u otro set. | `my_set.update(["Python", "Git"])` |
| `.remove(x)` | Elimina el elemento `x`. Lanza `KeyError` si el elemento no existe. | `my_set.remove("Alonso")` |
| `.discard(x)` | Elimina el elemento `x` si existe; si no existe, **no** lanza error. | `my_set.discard("España")` |
| `.pop()` | Elimina y devuelve un elemento arbitrario del set. | `item = my_set.pop()` |
| `.clear()` | Elimina todos los elementos dejando el conjunto vacío (`set()`). | `my_set.clear()` |
| `.union(otro)` o `\|` | Devuelve un nuevo set con todos los elementos únicos de ambos conjuntos. | `my_set.union(my_other_set)` |
| `.difference(otro)` o `-` | Devuelve los elementos que están en el primer set pero **no** en el segundo. | `my_new_set.difference(my_set)` |
| `.intersection(otro)` o `&` | Devuelve un nuevo set solo con los elementos en común entre ambos. | `my_new_set.intersection(my_set)` |
| `.symmetric_difference(otro)` o `^` | Devuelve los elementos que están en uno u otro set, pero **no** en ambos. | `set_a.symmetric_difference(set_b)` |
| `.issubset(otro)` o `<=` | Devuelve `True` si todos los elementos del set están contenidos en `otro`. | `set_a.issubset(set_b)` |
| `.issuperset(otro)` o `>=` | Devuelve `True` si el set contiene todos los elementos de `otro`. | `set_b.issuperset(set_a)` |
| `.isdisjoint(otro)` | Devuelve `True` si ambos sets no tienen ningún elemento en común. | `set_a.isdisjoint(set_b)` |

---

---

## `07_dicts.py` - Diccionarios (Dictionaries)

Un **diccionario** (`dict`) es una colección **mutable**, **indexada por claves** y **ordenada** (a partir de Python 3.7 mantiene el orden de inserción) que almacena datos en pares **`clave: valor`** (*key-value*). No permite claves duplicadas, aunque los valores sí pueden repetirse y ser de cualquier tipo de dato (incluyendo listas, sets u otros diccionarios).

### ¿Cuándo y por qué usar un Diccionario?
* **Representar entidades estructuradas:** Son ideales para modelar objetos o registros con atributos nombrados (como un usuario, un producto o respuestas en formato JSON), haciendo el código mucho más legible que acceder por índices numéricos.
* **Búsqueda directa por clave:** Al igual que los sets, usan tablas *hash* internamente, permitiendo acceder, modificar o verificar una clave de forma instantánea sin importar el tamaño del diccionario.

### Conceptos y Operaciones Clave

* **Creación:**
  * Vacíos: `my_dict = dict()` o `my_other_dict = {}`.
  * Con datos mixtos y anidados: Las claves deben ser tipos **inmutables** (`str`, `int`, `float`, `tuple`), mientras que los valores pueden ser cualquier objeto (ej. `"Lenguajes": {"Python", "Swift", "Kotlin"}` o `1: 1.77`).
* **Acceso, modificación y creación de claves:**
  * **Lectura:** `my_dict["Nombre"]` o `my_dict[1]`. (Si la clave no existe, lanza un `KeyError`).
  * **Actualización:** Si la clave ya existe, reasignarla actualiza su valor (`my_dict["Nombre"] = "Alonso"`).
  * **Inserción:** Si la clave no existe, asignarle un valor la crea automáticamente (`my_dict["Calle"] = "Calle falsa 123"`).
* **Eliminación:**
  * `del my_dict["Calle"]` elimina el par clave-valor específico del diccionario.
* **Comprobación con `in`:**
  * El operador `in` busca **únicamente entre las claves**, no entre los valores:
    * `"Nombre" in my_dict` devuelve `True` (es una clave).
    * `"Marín" in my_dict` devuelve `False` (es un valor; para buscar en valores se usa `"Marín" in my_dict.values()`).
* **Creación desde plantillas (`fromkeys`):**
  * `dict.fromkeys(("Nombre", 1))` genera un nuevo diccionario tomando un iterable como claves y asignándoles `None` (o un valor por defecto opcional) a todas.

### Métodos principales de Diccionarios

| Método | Descripción | Ejemplo |
| :--- | :--- | :--- |
| `.keys()` | Devuelve un objeto vista con todas las **claves** del diccionario. | `my_dict.keys()` |
| `.values()` | Devuelve un objeto vista con todos los **valores** del diccionario. | `my_dict.values()` |
| `.items()` | Devuelve una lista de tuplas `(clave, valor)` con cada par del diccionario. | `my_dict.items()` |
| `.get(clave, default)` | Obtiene el valor de una clave de forma segura. Si no existe, devuelve `None` (o `default`) sin lanzar error. | `my_dict.get("Telefono", "N/A")` |
| `.update(otro_dict)` | Actualiza el diccionario con los pares clave-valor de otro diccionario (sobrescribe claves repetidas). | `my_dict.update({"Pais": "CR"})` |
| `.pop(clave)` | Elimina la clave especificada y devuelve su valor asociado. | `edad = my_dict.pop("Edad")` |
| `.popitem()` | Elimina y devuelve el último par `(clave, valor)` insertado como una tupla. | `ultimo = my_dict.popitem()` |
| `.setdefault(k, val)` | Devuelve el valor de `k` si existe; si no existe, inserta `k` con el valor `val` y lo devuelve. | `my_dict.setdefault("Activo", True)` |
| `.fromkeys(seq, val)` | Crea un nuevo diccionario usando los elementos de `seq` como claves y `val` como valor inicial. | `dict.fromkeys(("Nombre", 1))` |
| `.copy()` | Devuelve una copia superficial (*shallow copy*) del diccionario. | `copia = my_dict.copy()` |
| `.clear()` | Elimina todos los elementos dejando el diccionario vacío `{}`. | `my_dict.clear()` |

---

---

## `08_conditionals.py` - Condicionales (Conditionals)

Las **estructuras condicionales** permiten controlar el flujo de ejecución de un programa, tomando decisiones para ejecutar distintos bloques de código según si una o varias condiciones se evalúan como verdaderas (`True`) o falsas (`False`).

### Conceptos y Reglas Clave

* **Indentación obligatoria (Sangría):** A diferencia de otros lenguajes que usan llaves `{}`, Python delimita los bloques de código mediante **indentación** (por convención **4 espacios** según PEP 8) después de los dos puntos `:`. Todo lo que esté al mismo nivel de sangría pertenece al mismo bloque; al volver al nivel base (como `print("Fin del programa")`), el código se ejecuta siempre fuera de la condición.
* **Evaluación implícita (*Truthy* y *Falsy*):**
  * Escribir `if my_condition:` es equivalente a `if bool(my_condition) == True:`.
  * **Valores *Falsy* (se evalúan como `False`):** `False`, `None`, `0`, `0.0`, cadenas vacías `""`, y colecciones vacías (`[]`, `()`, `{}`, `set()`).
  * **Valores *Truthy* (se evalúan como `True`):** Cualquier número distinto de cero (como `25` en `5 * 5`), cadenas con texto o colecciones con al menos un elemento.
* **Condiciones compuestas:** Se combinan expresiones relacionales (`==`, `!=`, `>`, `<`, `>=`, `<=`) con operadores lógicos (`and`, `or`, `not`), como en `my_condition > 10 and my_condition < 20`.
* **Orden de evaluación exclusivo:** En una cadena `if` -> `elif` -> `else`, Python evalúa de arriba hacia abajo y **ejecuta únicamente el primer bloque cuya condición sea `True`**, ignorando el resto.

### Estructura y Palabras Clave

| Palabra Clave | Descripción | Comportamiento |
| :--- | :--- | :--- |
| `if` | Evalúa la condición principal. | Ejecuta su bloque solo si la expresión resulta `True`. |
| `elif` | Abreviatura de *else if*. Permite encadenar condiciones adicionales. | Solo se evalúa si todas las condiciones `if` y `elif` anteriores fueron `False`. Puede haber tantos `elif` como sean necesarios. |
| `else` | Bloque por defecto o de respaldo. No lleva condición. | Se ejecuta únicamente cuando ninguna de las condiciones anteriores se cumplió. Es opcional. |

### Extras Útiles en Condicionales

* **Operador Ternario (Condicional en una línea):** Útil para asignaciones simples basadas en una condición:
  ```python
  mensaje = "Es 25" if my_condition == 25 else "No es 25"
---

---

## `09_loops.py` - Bucles o Ciclos (Loops)

Los **bucles** (*loops*) permiten ejecutar un mismo bloque de código repetidamente mientras se cumpla una condición o mientras se recorren los elementos de una colección de datos. Python cuenta con dos tipos principales de bucles: **`while`** y **`for`**.

### 1. Bucle `while` (Condicional)
Repite un bloque de código **mientras** una condición lógica se evalúe como `True`.

* **Actualización obligatoria:** Es fundamental modificar la variable de control dentro del ciclo (ej. `my_condition += 1`), de lo contrario se creará un **bucle infinito**.
* **Bloque `else` en `while` (Opcional):** A diferencia de otros lenguajes, en Python un bucle `while` puede llevar un bloque `else` que se ejecuta automáticamente **solo cuando la condición pasa a ser `False` de manera natural** (no se ejecuta si el bucle se detuvo con un `break`).

### 2. Bucle `for` (Iterativo)
Se utiliza para recorrer o **iterar** sobre cualquier objeto iterable de Python: listas (`list`), tuplas (`tuple`), conjuntos (`set`), cadenas de texto (`str`), rangos (`range()`) y diccionarios (`dict`).

* **Iteración en diccionarios:**
  * `for k in my_dict:` recorre las **claves** por defecto.
  * `for v in my_dict.values():` recorre los **valores**.
  * `for k, v in my_dict.items():` recorre **clave y valor** simultáneamente.

### Sentencias de Control de Bucles

Tanto `while` como `for` admiten palabras clave para alterar el flujo normal de las repeticiones:

| Sentencia | Descripción | Comportamiento en tu código |
| :--- | :--- | :--- |
| `break` | Detiene y **sale por completo** del bucle de inmediato, sin importar si quedan iteraciones pendientes ni ejecutar el `else`. | Al llegar a `15` en el `while` o a `3` en el `for`, interrumpe el ciclo y continúa con el resto del programa. |
| `continue` | **Salta la iteración actual** omitiendo el código restante debajo de él, y pasa directamente a la siguiente repetición del bucle. | Cuando `element == 3`, evita imprimir su valor y continúa directamente con el `4` y el `5`. |
| `pass` | Operación nula; se usa como marcador de posición cuando la sintaxis exige un bloque de código pero aún no se ha implementado lógica. | `for x in lista: pass` |

### Extras Útiles con Bucles `for`

* **Función `range(inicio, fin, paso)`:** Genera secuencias numéricas para repetir una acción un número exacto de veces (ej. `for i in range(5):` itera del `0` al `4`).
* **Función `enumerate(iterable)`:** Permite obtener tanto el **índice** como el **valor** en cada vuelta:
  ```python
  for indice, valor in enumerate(my_list):
      print(f"Índice {indice}: {valor}")

---

---

## `10_functions.py` - Funciones (Functions)

Una **función** es un bloque de código reutilizable y organizado que realiza una tarea específica. Se definen utilizando la palabra clave **`def`**, seguida del nombre de la función (en *snake_case*), paréntesis `()` y dos puntos `:`.

### ¿Por qué usar Funciones?
* **Reutilización de código (Principio DRY - *Don't Repeat Yourself*):** Evita duplicar lógica; defines la tarea una vez y la invocas cuantas veces necesites (`my_function()`).
* **Modularidad y legibilidad:** Divide problemas grandes en piezas pequeñas, fáciles de leer, probar y mantener.
* **Polimorfismo dinámico en Python:** Como Python es de tipado dinámico, una misma función como `sum_two_values(a, b)` puede sumar enteros (`5 + 7`), decimales (`4.5 + 4.2`) o concatenar cadenas de texto (`"Hola" + "Pura vida"`), siempre que los tipos sean compatibles entre sí.

### Conceptos y Tipos de Funciones

* **Sin parámetros ni retorno:** Ejecutan una acción directa (como imprimir un mensaje) y devuelven `None` de manera implícita.
* **Con parámetros (Entrada de datos):** Reciben información externa para procesarla.
  * **Argumentos posicionales:** Se asignan según el orden en que fueron definidos (`sum_two_values(5, 7)`).
  * **Argumentos por palabra clave (*Keyword Arguments*):** Se pasan indicando el nombre del parámetro, permitiendo alterar el orden (`print_name(surname="Marín", name="David")`).
* **Con valor de retorno (`return`):** Procesan datos y devuelven un resultado que puede almacenarse en una variable (`my_result = sum_two_values_with_return(10, 5)`) para seguir utilizándolo en otras partes del programa. Al ejecutarse `return`, la función finaliza inmediatamente.

### Extras Útiles en Funciones

| Característica | Descripción | Ejemplo |
| :--- | :--- | :--- |
| **Parámetros por defecto** | Asignan un valor predeterminado si no se envía ese argumento al llamar la función. | `def saludar(nombre, alias="Sin alias"):` |
| **`*args` (Argumentos arbitrarios)** | Permite recibir una cantidad variable de argumentos posicionales como una **tupla**. | `def listar(*elementos):` |
| **`**kwargs` (Keyword args arbitrarios)** | Permite recibir una cantidad variable de argumentos nombrados como un **diccionario**. | `def perfil(**datos):` |
| **Funciones `lambda`** | Funciones anónimas de una sola expresión, útiles para operaciones cortas. | `doble = lambda x: x * 2` |

---

---

## `11_classes.py` - Clases y Programación Orientada a Objetos (POO)

Una **clase** (`class`) es una plantilla o plano que define las características (**atributos**) y comportamientos (**métodos**) que tendrán los objetos creados a partir de ella (**instancias**). Por convención **PEP 8**, los nombres de las clases se escriben en formato *PascalCase* / *CamelCase* (ej. `Person`, `Estudiante`).

### Conceptos Fundamentales de POO en Python

* **Constructor (`__init__`) y `self`:**
  * `__init__` es el método especial que se ejecuta automáticamente al instanciar un objeto (ej. `my_person = Person("David", 25)`).
  * `self` hace referencia a la propia instancia del objeto que se está creando o manipulando, y debe ir siempre como primer parámetro de los métodos de instancia.
* **Atributos y Encapsulamiento:**
  * **Atributos públicos:** Se acceden y modifican directamente desde fuera de la clase (ej. `self.full_name`).
  * **Atributos privados (`__`):** Al anteponer doble guion bajo (ej. `self.__name`), Python aplica *name mangling* para restringir el acceso directo desde el exterior, protegiendo el dato y obligando a leerlo o modificarlo mediante métodos controlados (*getters* y *setters*, como `get_name()`).
* **Métodos:** Son funciones definidas dentro de una clase que describen las acciones que el objeto puede realizar (ej. `walk()`, `study()`).
* **Herencia y `super()`:**
  * Permite crear una clase hija que reutiliza y extiende los atributos y métodos de una clase padre: `class Estudiante(Person2):`.
  * La función `super().__init__(...)` invoca al constructor de la clase padre para inicializar los atributos heredados antes de agregar los propios de la subclase (como `self.student_id`).

### Resumen de Elementos en Clases

| Elemento | Descripción | Ejemplo en tu código |
| :--- | :--- | :--- |
| `class NombreClase:` | Define una nueva clase u objeto modelo. | `class Person2:` |
| `def __init__(self, ...):` | Método constructor que inicializa el estado del objeto. | `def __init__(self, name, surname):` |
| `self.atributo` | Define una propiedad pública asociada a cada instancia. | `self.full_name = f"{name} {surname}"` |
| `self.__atributo` | Define un atributo privado encapsulado dentro de la clase. | `self.__name = name` |
| `class Hija(Padre):` | Establece una relación de herencia entre clases. | `class Estudiante(Person2):` |
| `super()` | Permite acceder a métodos o al constructor de la clase padre. | `super().__init__(name, surname)` |

### Conceptos Avanzados de POO en Python

Para llevar el manejo de clases a un nivel más profesional y *Pythónico*, conviene tener en cuenta los siguientes elementos:

* **Atributos de Clase vs. Atributos de Instancia:**
  * **Atributos de instancia (`self.name`):** Pertenecen únicamente a cada objeto creado; modificarlo en uno no afecta a los demás.
  * **Atributos de clase:** Se definen directamente dentro de la clase (fuera de `__init__`) y **son compartidos por todas las instancias** (ej. `especie = "Humano"`).
* **Métodos Mágicos / Dunder Methods (`__str__`, `__repr__`):**
  * Son métodos especiales rodeados de doble guion bajo que personalizan el comportamiento nativo de los objetos. Por ejemplo, `__str__` define qué texto se muestra al hacer `print(objeto)` en lugar de imprimir su dirección en memoria:
    ```python
    def __str__(self):
        return f"{self.full_name} (ID: {self.student_id})"
    ```
* **Decorador `@property` (Getters y Setters *Pythónicos*):**
  * Permite acceder y validar atributos privados como si fueran atributos públicos normales, sin necesidad de llamar a métodos explícitos como `get_name()`:
    ```python
    @property
    def name(self):
        return self.__name
    ```
* **Polimorfismo y Sobrescritura (*Method Overriding*):**
  * Una subclase puede redefinir un método heredado de su clase padre (usando el mismo nombre) para darle un comportamiento especializado.
* **Decoradores `@classmethod` y `@staticmethod`:**
  * **`@classmethod`:** Recibe la clase (`cls`) en lugar de la instancia (`self`) como primer parámetro; se utiliza comúnmente para crear constructores alternativos.
  * **`@staticmethod`:** No recibe ni `self` ni `cls`; funciona como una utilidad auxiliar agrupada dentro de la clase por relación lógica.

---

## `12_exceptions.py` - Manejo de Excepciones (Exception Handling)

Una **excepción** es un error que ocurre durante la ejecución de un programa (*runtime error*) y que, si no se controla, detiene abruptamente el flujo normal de ejecución. El manejo de excepciones permite interceptar estos fallos, mostrar mensajes descriptivos o ejecutar acciones de recuperación para que el programa continúe funcionando de forma segura.

### Estructura Completa (`try` - `except` - `else` - `finally`)

| Bloque | Obligatorio | Comportamiento |
| :--- | :--- | :--- |
| `try` | Sí | Contiene el código susceptible de lanzar un error (ej. sumar tipos incompatibles como `int` y `str`). |
| `except` | Sí | Se ejecuta **únicamente si ocurre una excepción** dentro del `try`. Puede ser genérico o filtrar por un tipo específico de error. |
| `else` | No | Se ejecuta **solo si el bloque `try` finalizó sin ningún error** (útil para separar el código normal del código que se protege). |
| `finally` | No | Se ejecuta **siempre**, haya ocurrido una excepción o no (ideal para cerrar archivos, liberar recursos o conexiones a bases de datos). |

### Conceptos y Buenas Prácticas Clave

* **Captura por tipo de excepción:** Especificar la clase exacta del error (`except TypeError:`, `except ValueError:`) permite dar respuestas distintas según la causa del fallo en lugar de atrapar todo a ciegas.
* **Orden de especificidad:** Las excepciones más específicas deben ir primero y las más generales (como `except Exception as exception:`) al final, ya que Python evalúa los bloques `except` de arriba hacia abajo y ejecuta solo el primero que coincida.
* **Obtener el detalle del error (`as`):** Usar `except Exception as error:` guarda la instancia del error en una variable, permitiendo inspeccionar o registrar el mensaje técnico exacto que generó Python (`print(error)`).
* **Evitar `except:` vacío en producción:** Aunque es válido para pruebas rápidas, atrapar excepciones sin especificar al menos `Exception` puede ocultar interrupciones del sistema (como `KeyboardInterrupt` al detener el programa con `Ctrl + C`).

### Excepciones Comunes en Python

| Excepción | Cuándo ocurre | Ejemplo |
| :--- | :--- | :--- |
| `TypeError` | Operación o función aplicada a un tipo de dato incompatible. | `10 + "12"` |
| `ValueError` | El tipo de dato es correcto, pero su valor no es válido. | `int("hola")` |
| `ZeroDivisionError` | Intento de dividir o sacar módulo entre cero. | `10 / 0` |
| `IndexError` | Índice fuera del rango válido de una lista, tupla o string. | `[1, 2][5]` |
| `KeyError` | Búsqueda de una clave inexistente en un diccionario. | `{"a": 1}["b"]` |
| `NameError` | Uso de una variable o función que no ha sido definida. | `print(variable_inexistente)` |
| `FileNotFoundError` | Intento de abrir un archivo en una ruta que no existe. | `open("no_existe.txt")` |
| `AttributeError` | Intento de acceder a un método o atributo inexistente en un objeto. | `"texto".append("a")` |

### Extra Útil: Lanzar Excepciones Manualmente (`raise`)
Puedes forzar una excepción intencionalmente cuando se incumple una regla de negocio en tu código:
```python
if edad < 0:
    raise ValueError("La edad no puede ser un número negativo")
```

---

## `13_modules.py` - Módulos (Modules)

Un **módulo** es simplemente cualquier archivo con extensión `.py` que contiene definiciones de funciones, clases, variables o constantes listas para ser reutilizadas en otros archivos. Dividir un proyecto en módulos permite mantener el código ordenado, escalable y fácil de mantener.

### Formas de Importar Módulos

| Sintaxis | Descripción | Ejemplo |
| :--- | :--- | :--- |
| `import modulo` | Importa el módulo completo. Para usar sus funciones se antepone su nombre (`modulo.funcion()`). | `import math` -> `math.pow(2, 3)` |
| `from modulo import item` | Importa únicamente funciones, clases o constantes específicas para usarlas directamente sin prefijo. | `from my_module import printValue, sum` |
| `import modulo as alias` | Importa el módulo asignándole un nombre corto o alias (muy común en ciencia de datos). | `import statistics as stats` |
| `from modulo import item as alias` | Importa un elemento específico y le asigna un alias para evitar conflictos de nombres. | `from math import pi as PI_VALUE` |

### Reglas y Buenas Prácticas Clave

* **Nomenclatura de archivos importables:** Para que un archivo `.py` pueda ser importado como módulo, su nombre **debe seguir las mismas reglas que las variables** (comenzar con una letra o guion bajo `_` y no contener guiones medios `-` ni espacios). Por ejemplo, `10_functions.py` no puede importarse con `import 10_functions` porque empieza con un número.
* **Cada módulo contiene múltiples herramientas:** Un solo módulo agrupa decenas o cientos de funciones, constantes y clases relacionadas entre sí. Puedes explorar todo lo que contiene cualquier módulo ejecutando `dir(nombre_modulo)` o consultando su ayuda con `help(nombre_modulo)`.
* **Tipos de módulos en Python:**
  1. **Módulos propios:** Archivos `.py` creados por ti dentro de tu proyecto (ej. `my_module.py`).
  2. **Módulos de la Biblioteca Estándar (*Built-in*):** Vienen preinstalados con Python listos para usar sin instalar nada extra (ej. `math`, `random`, `os`).
  3. **Módulos de terceros:** Paquetes creados por la comunidad que se instalan mediante `pip` desde [PyPI](https://pypi.org/) (ej. `requests`, `pandas`, `numpy`).

### Módulos más utilizados de la Biblioteca Estándar

Python cuenta con más de 200 módulos integrados. Estos son algunos de los más habituales en el desarrollo diario:

| Módulo | Propósito principal | Ejemplos de funciones / constantes |
| :--- | :--- | :--- |
| `math` | Operaciones matemáticas avanzadas y constantes. | `math.pi`, `math.sqrt()`, `math.pow()`, `math.ceil()`, `math.floor()` |
| `random` | Generación de números pseudoaleatorios y selecciones al azar. | `random.random()`, `random.randint(1, 10)`, `random.choice(lista)` |
| `datetime` | Manejo y formateo de fechas, horas e intervalos de tiempo. | `datetime.now()`, `date.today()`, `timedelta()` |
| `os` | Interacción con el sistema operativo, rutas, carpetas y variables de entorno. | `os.getcwd()`, `os.listdir()`, `os.mkdir()`, `os.environ` |
| `sys` | Acceso a parámetros y funciones propias del intérprete de Python. | `sys.argv`, `sys.exit()`, `sys.version`, `sys.path` |
| `json` | Conversión entre objetos de Python (diccionarios/listas) y texto en formato JSON. | `json.loads()`, `json.dumps()`, `json.load()`, `json.dump()` |
| `re` | Búsqueda y manipulación avanzada de texto mediante expresiones regulares (*Regex*). | `re.search()`, `re.findall()`, `re.sub()`, `re.match()` |
| `statistics` | Funciones estadísticas básicas sobre datos numéricos. | `statistics.mean()`, `statistics.median()`, `statistics.mode()` |

* **Índice oficial completo:** Puedes consultar la lista completa de todos los módulos integrados y sus funciones en la [Documentación Oficial de la Biblioteca Estándar de Python](https://docs.python.org/es/3/library/index.html).

---

## 📚 Material Adicional y Créditos

Este repositorio de práctica está inspirado y estructurado tomando como base el excelente curso y guía paso a paso de **Asabeneh Yetayeh**:

* **Repositorio de referencia completo:** [Asabeneh / 30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python)
  * *Descripción:* Un reto de programación de 30 días que cubre desde los fundamentos de Python hasta estructuras de datos, funciones, programación orientada a objetos, manejo de archivos, expresiones regulares, análisis de datos (`NumPy`, `Pandas`) y desarrollo web (`Flask`).