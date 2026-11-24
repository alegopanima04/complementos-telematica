# Seminario 1 - Complementos de Telemática

**Nombre:** Alejandro Gómez-Pardo Nieto-Márquez

## Descripción

He creado un programa sencillo en Python que calcula el tiempo aproximado que tarda en descargarse un archivo, dependiendo de su tamaño en MB y de la velocidad de internet en Mbps.

El programa muestra el resultado en segundos y también en minutos y segundos para que sea más fácil de entender.

## Cómo ejecutarlo

1. Descargar el archivo `calculadora_descarga.py`.
2. Abrirlo con VS Code.
3. Ejecutarlo desde la terminal con el comando:

   `python calculadora_descarga.py`

4. Introducir el tamaño del archivo y la velocidad de internet.

## Uso de GitHub Copilot

Para realizar el programa he utilizado el chat de GitHub Copilot en VS Code.

**Prompt utilizado:**

> Quiero crear un programa sencillo en Python que calcule cuánto tarda en descargarse un archivo según su tamaño en MB y la velocidad de internet en Mbps.
>
> El programa debe pedir el tamaño del archivo en MB y la velocidad de conexión en Mbps, calcular el tiempo de descarga en segundos y sacar el resultado por pantalla.
>
> Utiliza código básico de Python, sin librerías externas, y añade comentarios sencillos para que pueda entenderlo. Crea el archivo calculadora_descarga.py.

Después de generar el código, le pregunté a Copilot por qué se multiplicaba el tamaño del archivo por 8. Me explicó que era necesario convertir los megabytes en megabits, ya que la velocidad se mide en Mbps.

**Modificación personal:**

He añadido por mi cuenta el cálculo de los minutos y segundos utilizando los operadores `//` y `%`, para que el tiempo no aparezca solamente como un número decimal de minutos.

Finalmente, he ejecutado el programa en VS Code y comprobado que funcionaba correctamente.
