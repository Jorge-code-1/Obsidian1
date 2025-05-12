## ¿Cómo definir el comportamiento en las clases con métodos personalizados?

La programación orientada a objetos se centra en representar entidades del mundo real como "objetos" dentro de un software. Cada objeto tiene características (atributos) y comportamientos (métodos). En el lenguaje de programación C#, los métodos son funciones que definen el comportamiento de las clases, permitiendo ejecutar acciones internas. Ahora veremos cómo implementar métodos personalizados en nuestras clases, concretamente en una clase de superhéroe.

### ¿Cómo crear un método sin retorno en C#?

Para implementar un método en C#, primero se define su tipo de retorno. Un método sin retorno utiliza el tipo `void`, ejecutando acciones sin devolver valores. Aquí crearemos un método `UsarSuperpoderes` para iterar sobre los superpoderes de un superhéroe.

```csharp
public void UsarSuperpoderes()
{
    foreach (var item in superpoderes)
    {
        Console.WriteLine($"{nombre} está usando el superpoder {item.Nombre}!");
    }
}
```

- **Función `void`:** Significa que la función no devuelve ningún valor externo.
- **Iteración `foreach`:** Permite recorrer la colección `superpoderes` e imprimir un mensaje en la consola para cada superpoder.

Al invocar el método en el objeto `Superman`, se ejecuta así:

```csharp
Superman.UsarSuperpoderes();
```

### ¿Cómo crear un método que devuelve un valor?

Aunque los métodos `void` son útiles, frecuentemente necesitamos métodos que devuelvan valores. Aquí modificaremos `UsarSuperpoderes` para retornar un `string` con los superpoderes usados, usando la clase `StringBuilder`.

```csharp
public string UsarSuperpoderes()
{
    StringBuilder sb = new StringBuilder();
    foreach (var item in superpoderes)
    {
        sb.AppendLine($"{nombre} está usando el superpoder {item.Nombre}!");
    }
    return sb.ToString();
}
```

- **`StringBuilder`:** Facilita la concatenación de cadenas de texto.
- **`AppendLine`:** Añade líneas al `StringBuilder`.

Luego, al invocar este método y obtener el resultado:

```csharp
string resultSuperpoderes = Superman.UsarSuperpoderes();
Console.WriteLine(resultSuperpoderes);
```

Ambas formas de implementación tienen su utilidad dependiendo del contexto y necesidades del proyecto.

### ¿En qué casos utilizar métodos sin o con retorno?

- **Métodos `void`:** Son idóneos para acciones internas que no requieren comunicar resultados (p. ej., logging, actualizaciones de estado).
- **Métodos con retorno:** Útiles cuando es necesario procesar datos y devolver información al exterior para su posterior uso (p. ej., cálculos y transformaciones).

En resumen, aprovechar la capacidad de los métodos para definir comportamientos de tus clases permitirá crear software más modular y organizado. Continúa explorando C# para dominar otros conceptos importantes como estructuras y registros, que también potencian la creación de código eficiente en programación orientada a objetos.