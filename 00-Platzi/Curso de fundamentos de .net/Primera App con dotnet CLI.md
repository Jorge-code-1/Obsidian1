## ¿Cómo crear tu primer proyecto en .NET?

El mundo de la programación con .NET puede parecer un tanto abrumador al principio, pero con el conocimiento adecuado y una guía paso a paso, podrás crear tu primer proyecto en un abrir y cerrar de ojos. En esta lección, te mostraremos cómo dar los primeros pasos en este potente framework. Prepárate para entrar en acción y ver tu primer "Hello World" en la consola correr en tu máquina.

### ¿Cómo configurar el entorno inicial?

Antes de comenzar, es fundamental asegurarnos de que nuestro entorno está adecuadamente configurado. Utilizaremos la consola de comandos, y lo bueno es que el CLI de .NET funciona perfectamente sin importar en qué parte de la estructura de directorios te encuentres en Windows. Si utilizas otro sistema operativo, algunos comandos pueden variar ligeramente, pero el objetivo sigue siendo el mismo: crear una estructura de carpetas para alojar nuestro proyecto.

- Navega hasta la raíz de tu sistema (en este caso, la ruta C).
    
- Crea un nuevo directorio con el comando:
    
    ```shell
    mkdir platzi
    ```
    
- Accede a este directorio y luego crea uno adicional para tu aplicación de consola:
    
    ```shell
    cd platzi
    mkdir console-app
    cd console-app
    ```
    

### ¿Cómo crear un proyecto de consola en .NET?

Una vez que tengas tu directorio configurado, el siguiente paso es crear el proyecto de consola. Esto implica el uso del comando `.netnew console`, que creará la estructura básica del proyecto.

- Verifica que estás en el directorio correcto (console-app).
    
- Ejecuta el comando para crear el proyecto:
    
    ```shell
    dotnet new console
    ```
    

### ¿Qué opciones de plantillas existen en .NET?

El comando `.netnew` ofrece una variedad impresionante de plantillas para diferentes tipos de proyectos en .NET. Si deseas explorar todas las opciones disponibles:

- Ejecuta el siguiente comando para listar todas las plantillas:
    
    ```shell
    dotnet new list
    ```
    

Este listado te mostrará opciones como proyectos de prueba de unidades con NUnit o XUnit, y proyectos para crear aplicaciones de escritorio usando WPF, entre otros. Estas plantillas permiten flexibilidad para crear soluciones ajustadas a tus necesidades específicas.

### ¿Cómo ejecutar tu primer proyecto?

Una vez creado el proyecto, es momento de comprobar que todo está en orden y ver el resultado en acción. Este es un paso crucial porque permite verificar que el proyecto se ha configurado correctamente.

- Ejecuta el comando para restaurar las dependencias:
    
    ```shell
    dotnet restore
    ```
    
- Corre el proyecto con el siguiente comando:
    
    ```shell
    dotnet run
    ```
    

Al ejecutar estos comandos, la consola debería mostrar el mensaje "Hello World". Este es el resultado predefinido del template para una aplicación de consola, confirmando que tu proyecto se ejecuta correctamente.

Finalmente, has creado con éxito tu primer proyecto en .NET. Con esta base, estás listo para explorar funciones más complejas y capacidades avanzadas que este framework ofrece. ¡Sigue explorando y aprendiendo para llevar tus habilidades al siguiente nivel!

https://github.com/platzi/fundamentos-net/tree/90f7de8d06e46017d75c2787808dfe1a8f93d705