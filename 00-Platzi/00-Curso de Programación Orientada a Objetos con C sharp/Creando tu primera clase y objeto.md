## ¿Cómo crear tu primera clase y objeto en C#?

Comenzar a programar con un paradigma orientado a objetos puede parecer complejo, pero con una guía paso a paso, verás que es más sencillo de lo que parece. En este tutorial, aprenderás a crear tu propia clase y objeto en C#, usando Visual Studio y un proyecto de consola.

### ¿Qué es la programación orientada a objetos?

La programación orientada a objetos (OOP, por sus siglas en inglés) es un paradigma de programación que utiliza "objetos" para representar datos y métodos. Los objetos son instancias de clases, que actúan como plantillas que describen sus características y comportamientos. Esta metodología facilita la reutilización del código, mejora la organización y ayuda a simplificar el mantenimiento del mismo.

### ¿Cómo crear un proyecto en Visual Studio?

Para empezar a experimentar con la OOP, necesitas crear un proyecto básico en Visual Studio. Sigue estos pasos:

1. Abre Visual Studio 2022 y selecciona **Crear un nuevo proyecto**.
2. Elige **Proyecto de consola (.NET)**, ya que es la forma más sencilla de empezar a programar en C#.
3. Asigna un nombre y una ubicación al proyecto. Por ejemplo, "Programación Orientada a Objetos Demo".
4. Selecciona la versión de .NET, preferiblemente la última disponible.
5. Haz clic en **Crear**.

### ¿Qué objetos podemos representar en código?

Selecciona un objeto físico que tengas a tu alrededor. Puede ser cualquier cosa, como un monitor, una cámara o incluso un apuntador. Analiza las características del objeto. Por ejemplo, si usas un apuntador, podrías identificar las siguientes características:

- Color (negro, blanco, azul, etc.)
- Tamaño (en centímetros)
- Número de botones
- Si tiene o no sticker
- Marca y tipo de batería

### ¿Cómo definir una clase en C#?

Para definir una clase, utiliza la palabra clave `class` seguida del nombre que deseas para la misma. Por ejemplo, si estás creando la clase para un objeto apuntador, haz lo siguiente:

```csharp
public class Apuntador
{
    public string Color { get; set; }
    public double Largo { get; set; }
    public int NumeroDeBotones { get; set; }
    public bool TieneSticker { get; set; }
}
```

### ¿Cómo crear un objeto en C#?

Una vez definida la clase, puedes crear instancias u objetos de esta clase. Usa la palabra clave `new` para instanciar el objeto y asignar valores a sus propiedades:

```csharp
Apuntador apuntadorPlexi = new Apuntador
{
    Color = "Negro",
    Largo = 24.5,
    NumeroDeBotones = 3,
    TieneSticker = true
};

Apuntador apuntadorPlexi2 = new Apuntador
{
    Color = "Blanco",
    Largo = 24.5,
    NumeroDeBotones = 3,
    TieneSticker = false
};
```

### ¿Qué son los niveles de acceso?

En C#, controlamos la accesibilidad de las propiedades de las clases a través de modificadores de acceso. `public` permite el acceso desde cualquier parte del programa, asegurando que las propiedades se puedan modificar externamente según necesidades específicas de los objetos.

### ¿Por qué es útil la programación orientada a objetos?

La programación orientada a objetos facilita la creación de código modular y reutilizable. Los desarrolladores pueden crear plantillas (clases) y reutilizar sus definiciones para crear nuevos objetos con las mismas características y métodos, pero con valores diferentes. Esto no solo ahorra tiempo, sino que también fomenta un código organizado y fácil de mantener.

Para explorar este paradigma con profundidad, intenta aplicar estos conceptos a otros objetos que encuentres a tu alrededor y comparte tus experimentos con los demás estudiantes. ¡No te detengas aquí! Sigue adelante y mejora tus habilidades en OOP con el curso.