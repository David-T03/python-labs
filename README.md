# python-labs
Un repositorio en donde se aprenderá lo básico de Python

# Funciones Integradas (Built-in) en Python - Cheat Sheet

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

## Convenciones para Nombres de Variables en Python

A continuación se muestran ejemplos válidos de nombres de variables:

* Nombres de una sola palabra en minúsculas como `firstname`, `lastname`, `age`, `country` y `city`.
* Nombres compuestos separados por guiones bajos (*snake_case*) como `first_name`, `last_name`, `capital_city` y `birth_year`.
* Uso de números integrados o al final como `year2021`, `year_2021`, `current_year_2021`, `num1` y `num2`.
* Uso de un guion bajo inicial (`_if`) para evitar conflictos si se desea utilizar una palabra reservada como variable.

## Operadores en Python

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

---

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
| `|=` | `x \|= 3` | `x = x \| 3` |
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

---

### Operadores Lógicos

Se utilizan para combinar declaraciones condicionales.

| Operador | Descripción | Ejemplo |
| :--- | :--- | :--- |
| `and` | Devuelve `True` si ambas afirmaciones son verdaderas | `x < 5 and x < 10` |
| `or` | Devuelve `True` si al menos una de las afirmaciones es verdadera | `x < 5 or x < 4` |
| `not` | Invierte el resultado; devuelve `False` si el resultado es verdadero | `not(x < 5 and x < 10)` |