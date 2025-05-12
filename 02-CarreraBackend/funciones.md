En Python, **las funciones** te permiten agrupar instrucciones que realizan una tarea específica y reutilizarlas cuando las necesites. Son fundamentales para escribir código limpio y organizado.

---

### 🔧 ¿Cómo se define una función?

```python
def nombre_de_la_funcion(parámetros):
    # bloque de código
    return resultado
```

---

### 📌 Ejemplos básicos

#### 1. **Función sin parámetros ni retorno**

```python
def saludar():
    print("Hola, ¿cómo estás?")

saludar()
```

---

#### 2. **Función con parámetros**

```python
def saludar_persona(nombre):
    print(f"Hola, {nombre}!")

saludar_persona("Ana")
```

---

#### 3. **Función con retorno**

```python
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print("Resultado:", resultado)
```

---

#### 4. **Parámetros por defecto**

```python
def saludar(nombre="invitado"):
    print(f"Hola, {nombre}")

saludar()          # Usa el valor por defecto
saludar("María")   # Usa el valor pasado
```

---

#### 5. **Retornar múltiples valores**

```python
def operaciones(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

s, r = operaciones(10, 4)
print("Suma:", s)
print("Resta:", r)
```

---

### 🧠 ¿Querés algunos ejercicios para practicar funciones?
¡Perfecto! Aquí tenés una serie de **ejercicios prácticos para aprender funciones en Python**, desde nivel básico hasta un poco más avanzado:

---

### 🧪 **Ejercicios de práctica – Funciones en Python**

#### 🔸 1. Función que imprima un saludo

```python
# Crea una función que imprima "¡Hola mundo!".
def saludar():
    print("¡Hola mundo!")

saludar()
```

---

#### 🔸 2. Función con un parámetro

```python
# Crea una función que reciba un nombre y lo salude.
def saludar_persona(nombre):
    print(f"Hola, {nombre}!")

saludar_persona("Lucía")
```

---

#### 🔸 3. Función que devuelva el cuadrado de un número

```python
def cuadrado(numero):
    return numero ** 2

print(cuadrado(4))  # Debería imprimir 16
```

---

#### 🔸 4. Función que calcule el área de un triángulo

```python
def area_triangulo(base, altura):
    return (base * altura) / 2

print(area_triangulo(10, 5))  # Debería imprimir 25.0
```

---

#### 🔸 5. Función con valor por defecto

```python
def saludar(nombre="invitado"):
    print(f"Bienvenido, {nombre}!")

saludar()
saludar("Juan")
```

---

#### 🔸 6. Función que devuelva si un número es par

```python
def es_par(numero):
    return numero % 2 == 0

print(es_par(4))  # True
print(es_par(7))  # False
```

---

#### 🔸 7. Función que reciba una lista de números y devuelva su suma

```python
def sumar_lista(lista):
    return sum(lista)

print(sumar_lista([1, 2, 3, 4, 5]))  # 15
```

---

#### 🔸 8. Función que devuelva el mayor de tres números

```python
def mayor_de_tres(a, b, c):
    return max(a, b, c)

print(mayor_de_tres(10, 25, 17))  # 25
```

---

