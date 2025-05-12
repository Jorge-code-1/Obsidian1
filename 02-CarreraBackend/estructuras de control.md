En Python, las **estructuras de control** te permiten dirigir el flujo de tu programa: decidir qué ejecutar, cuántas veces y bajo qué condiciones.

A continuación te las explico con ejemplos sencillos:

---

### 🔁 1. **Condicionales (`if`, `elif`, `else`)**

```python
edad = 20

if edad < 18:
    print("Es menor de edad")
elif edad == 18:
    print("Tiene 18 años")
else:
    print("Es mayor de edad")
```

---

### 🔁 2. **Bucles (`while`)**

```python
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1
```

---

### 🔁 3. **Bucles (`for`)**

```python
# Recorrer una lista
frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print("Fruta:", fruta)

# Recorrer un rango de números
for i in range(3):
    print("Número:", i)
```

---

### 🛑 4. **Control de flujo: `break` y `continue`**

```python
# break: salir del bucle
for i in range(10):
    if i == 5:
        break
    print("Número con break:", i)

# continue: saltear una iteración
for i in range(5):
    if i == 2:
        continue
    print("Número con continue:", i)
```

---

### 🧩 5. **Match-case (similar a switch, desde Python 3.10)**

```python
comando = "inicio"

match comando:
    case "inicio":
        print("El programa inicia")
    case "salir":
        print("El programa finaliza")
    case _:
        print("Comando desconocido")
```

---

¿Querés ejercicios prácticos para dominar estas estructuras?

¡Genial! Acá te dejo una serie de **ejercicios prácticos** para que practiques las estructuras de control en Python, organizados por tipo.

---

### 🧠 **Ejercicios de práctica – Estructuras de control**

#### 🔸 1. **Condicionales (`if`, `elif`, `else`)**

```python
# Ejercicio: Decir si un número es positivo, negativo o cero
numero = int(input("Ingresá un número: "))

if numero > 0:
    print("Es positivo")
elif numero < 0:
    print("Es negativo")
else:
    print("Es cero")
```

---

#### 🔸 2. **Bucle `while`**

```python
# Ejercicio: Contar hasta 5 con un while
contador = 1
while contador <= 5:
    print("Contando:", contador)
    contador += 1
```

---

#### 🔸 3. **Bucle `for`**

```python
# Ejercicio: Imprimir los números del 1 al 10
for i in range(1, 11):
    print(i)

# Ejercicio: Mostrar los caracteres de un texto
texto = "Python"
for letra in texto:
    print(letra)
```

---

#### 🔸 4. **`break` y `continue`**

```python
# Ejercicio: Encontrar el primer número divisible por 7 entre 10 y 100
for i in range(10, 101):
    if i % 7 == 0:
        print("El primer divisible por 7 es:", i)
        break

# Ejercicio: Imprimir todos los números del 1 al 10 excepto el 5
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
```

---

#### 🔸 5. **`match-case` (Python 3.10+)**

```python
# Ejercicio: Menú de opciones simple
opcion = input("Elegí una opción (a, b, c): ")

match opcion:
    case "a":
        print("Elegiste la opción A")
    case "b":
        print("Elegiste la opción B")
    case "c":
        print("Elegiste la opción C")
    case _:
        print("Opción inválida")
```

---

¿Querés que te los arme en un archivo `.py` o en un cuaderno Jupyter para practicar más cómodamente?