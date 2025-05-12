En Python, los tipos de datos más importantes se agrupan en **tipos primitivos** y **estructuras más complejas**. A continuación te los resumo con ejemplos:

---

### 🧱 Tipos de datos básicos (primitivos)

1. **`int`** – Enteros
    
    ```python
    x = 10
    ```
    
2. **`float`** – Números decimales
    
    ```python
    y = 3.14
    ```
    
3. **`bool`** – Booleanos (verdadero o falso)
    
    ```python
    es_activo = True
    ```
    
4. **`str`** – Cadenas de texto
    
    ```python
    nombre = "Juan"
    ```
    

---

### 📦 Tipos de datos compuestos (estructuras)

5. **`list`** – Lista ordenada y mutable
    
    ```python
    frutas = ["manzana", "banana", "naranja"]
    ```
    
6. **`tuple`** – Tupla ordenada e inmutable
    
    ```python
    coordenadas = (10.0, 20.5)
    ```
    
7. **`dict`** – Diccionario (clave-valor)
    
    ```python
    persona = {"nombre": "Ana", "edad": 30}
    ```
    
8. **`set`** – Conjunto (sin elementos repetidos)
    
    ```python
    numeros = {1, 2, 3}
    ```
    

---

### ⏳ Tipos especiales

9. **`NoneType`** – Representa la ausencia de valor
    
    ```python
    resultado = None
    ```
    

---

Ejercicios de practica 
¡Perfecto! Aquí tenés una serie de **ejercicios prácticos para principiantes** para que practiques los tipos de datos en Python:

---

### 🧠 **Ejercicios de práctica por tipo de dato**

#### 1. `int` y `float`

```python
# a. Suma dos números enteros
a = 15
b = 27
print("Suma:", a + b)

# b. Calculá el área de un círculo (radio = 5)
radio = 5
pi = 3.1416
area = pi * radio ** 2
print("Área del círculo:", area)
```

#### 2. `bool`

```python
# ¿Es mayor de edad?
edad = 20
es_mayor = edad >= 18
print("¿Es mayor de edad?", es_mayor)
```

#### 3. `str`

```python
# Concatená nombre y apellido
nombre = "Juan"
apellido = "Pérez"
nombre_completo = nombre + " " + apellido
print("Nombre completo:", nombre_completo)

# Largo del nombre completo
print("Cantidad de letras:", len(nombre_completo))
```

#### 4. `list`

```python
# Lista de compras
compras = ["pan", "leche", "huevos"]
compras.append("arroz")  # agregá un ítem
print("Lista de compras:", compras)
print("Primer ítem:", compras[0])
```

#### 5. `tuple`

```python
# Tupla de coordenadas
ubicacion = (34.5, -58.4)
print("Latitud:", ubicacion[0])
print("Longitud:", ubicacion[1])
```

#### 6. `dict`

```python
# Diccionario de usuario
usuario = {"nombre": "Lucía", "edad": 25}
print("Nombre:", usuario["nombre"])
usuario["email"] = "lucia@mail.com"  # agregá una clave
print("Usuario actualizado:", usuario)
```

#### 7. `set`

```python
# Conjunto de números (elimina duplicados)
numeros = {1, 2, 2, 3, 4, 4, 5}
print("Conjunto sin repetidos:", numeros)
```

#### 8. `NoneType`

```python
# Variable sin valor asignado
resultado = None
print("Resultado inicial:", resultado)
resultado = 42
print("Resultado después:", resultado)
```

---

¿Querés que te los prepare en un archivo `.py` para descargar y probar todo junto?