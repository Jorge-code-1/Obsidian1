## ¿Cómo crear un programa interactivo sencillo en .NET?

Entender los conceptos básicos de .NET puede parecer complicado, pero con la práctica adecuada, esto se vuelve más llevadero. Aquí te mostraremos cómo crear un pequeño programa que interactúa con el usuario, permitiéndote capturar algunos datos personales y presentar un resumen utilizando características esenciales de .NET.

### ¿Cuáles son los pasos iniciales para crear un programa de consola?

1. **Inicia un proyecto de consola**: Abre un proyecto de consola previamente creado en .NET.
2. **Elimina el contenido predeterminado**: Remueve el código por defecto del proyecto para tener un lienzo limpio donde trabajar.
3. **Solicita datos al usuario**:
    - Utiliza `Console.WriteLine` para pedirle al usuario que ingrese:
        - Su nombre.
        - Su cargo dentro de la empresa.
        - Su edad.
    - Usa `Console.ReadLine` para guardar cada una de estas entradas en variables denominadas `nombre`, `cargo` y `edad` respectivamente.

```csharp
Console.WriteLine("Por favor, ingrese su nombre:");
string nombre = Console.ReadLine();

Console.WriteLine("Por favor, ingrese su cargo:");
string cargo = Console.ReadLine();

Console.WriteLine("Por favor, ingrese su edad:");
string edad = Console.ReadLine();
```

### ¿Cómo presentar la información capturada de manera eficiente?

Una vez capturados los datos del usuario, puedes presentar un resumen usando la técnica de concatenación en C#:

- Utiliza la técnica de interpolación de cadenas para crear un mensaje personalizado incluyendo los datos.
- Esto puede ser particularmente útil para aplicaciones como plantillas de correos o la generación de documentos.

```csharp
Console.WriteLine($"Mi nombre es {nombre}, mi cargo es {cargo} y tengo {edad} años.");
```

### ¿Cómo ejecutar y compilar el proyecto de manera eficiente?

Ejecutar y verificar tu proyecto es crucial para asegurar su correcto funcionamiento:

1. **Compilación y ejecución**: Usa el comando `dotnet run` para ejecutar el programa.
2. **Verificación de compilación**: Para comprobar que no hay errores de sintaxis o dependencias faltantes, utiliza el comando `dotnet build`.
3. **Auto-recompilación**: Para observar cambios en tiempo real, `dotnet watch run` recompilará automáticamente cada vez que guardes un archivo.

```shell
dotnet run
dotnet build
dotnet watch run
```

### ¿Cuál es la importancia de gestionar las dependencias?

En proyectos más grandes o cuando se descargan desde repositorios, gestionar las librerías y dependencias correctamente es esencial:

- **Restauración de dependencias**: Utiliza `dotnet restore` para asegurar que todas las librerías requeridas están presentes.

```shell
dotnet restore
```

Este enfoque es sumamente efectivo para aprender los procesos de desarrollo en .NET, ayudándote a integrar prácticas profesionales en tus proyectos futuros. Recuerda practicar constantemente y experimentar con diferentes opciones para mejorar tus habilidades en este entorno de desarrollo. ¡Sigue explorando y programando en .NET!

https://github.com/platzi/fundamentos-net/tree/16---ejecucion