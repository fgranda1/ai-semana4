# 🔥 Juego de las Cerillas (Nim)

Este proyecto es una implementación sencilla del **Juego de las Cerillas
(Nim)** usando **Python** y **Tkinter**.

La idea del proyecto es llevar a la práctica algunos conceptos de
**Inteligencia Artificial**, especialmente el algoritmo **Minimax** y la
**Poda Alfa-Beta**. En lugar de dejar estos conceptos solamente en la
parte teórica, hice un pequeño juego donde una persona puede jugar
directamente contra la IA.

## ¿Cómo funciona el juego?

El juego comienza con **15 cerillas**.

En cada turno se pueden quitar:

-   1 cerilla
-   2 cerillas
-   3 cerillas

Hay una regla importante: **quien tome la última cerilla pierde**.

La persona juega primero y después de cada movimiento la IA analiza las
opciones disponibles para decidir cuántas cerillas quitar.

Cuando termina una partida, el juego vuelve a comenzar automáticamente
con 15 cerillas.

## ¿Qué hace la IA?

La IA utiliza **Minimax** para revisar las diferentes posibilidades que
puede tener el juego.

En cada turno, el algoritmo analiza los movimientos disponibles y trata
de escoger el que le dé el mejor resultado teniendo en cuenta también
las posibles respuestas del jugador.

También se utiliza **Poda Alfa-Beta**. Esta parte sirve para evitar que
el algoritmo tenga que revisar algunas posibilidades que ya no van a
cambiar la decisión final.

En este juego el número de opciones es pequeño, por lo que el algoritmo
puede analizar las jugadas rápidamente. Aun así, el ejemplo sirve para
entender cómo estos conceptos pueden llevarse a un programa que funciona
de manera interactiva.

## Interfaz

La interfaz está hecha con **Tkinter**, que permite crear la ventana y
los botones del juego directamente desde Python.

La ventana muestra:

-   Las cerillas que quedan.
-   La cantidad de cerillas restantes.
-   Los botones para quitar 1, 2 o 3 cerillas.
-   Un mensaje indicando cuándo es el turno de la persona o de la IA.
-   Un aviso cuando termina la partida.

## Requisitos

Para ejecutar el proyecto se necesita:

-   Python 3
-   Tkinter

El programa utiliza solamente módulos incluidos en Python:

``` python
import math
import tkinter as tk
from tkinter import messagebox
```

No se necesitan librerías externas para el funcionamiento del juego.

## Cómo ejecutar el proyecto

Primero se debe guardar el código en un archivo, por ejemplo:

``` text
main.py
```

Después, desde la terminal, se ejecuta:

``` bash
python3 main.py
```

En algunos equipos también puede funcionar con:

``` bash
python main.py
```

Al ejecutarlo debería aparecer la ventana del juego.

## Estructura general

El código está dividido principalmente en dos partes.

### 1. Algoritmo Minimax con Poda Alfa-Beta

En esta parte se encuentran las funciones que se encargan de analizar
las posibles jugadas:

-   `minimax_alfa_beta()`
-   `obtener_mejor_movimiento()`

La primera realiza la búsqueda y aplica la poda Alfa-Beta. La segunda
utiliza ese resultado para decidir qué movimiento debe hacer la IA.

### 2. Interfaz gráfica con Tkinter

La clase:

``` python
JuegoCerillasTkinter
```

se encarga de mostrar el juego y manejar la interacción con la persona.

Aquí se encuentran las funciones que actualizan las cerillas, reciben el
movimiento del jugador y hacen que la IA juegue después.

## ¿Qué aprendí con este ejercicio?

Con este ejercicio pude relacionar la parte teórica de la **búsqueda
adversarial** con algo más práctico.

Al principio, conceptos como Minimax y Poda Alfa-Beta pueden parecer un
poco abstractos porque se explican mediante árboles de decisiones y
diferentes posibilidades. Al llevarlos al Juego de las Cerillas, es más
fácil ver qué está haciendo el algoritmo en cada turno.

También pude practicar el uso de **Tkinter** para crear una interfaz
sencilla y conectar la lógica del programa con los botones y mensajes
que aparecen en pantalla.

## Tecnologías utilizadas

-   **Python**
-   **Tkinter**
-   **Minimax**
-   **Poda Alfa-Beta**

## Autor

**Felipe Granda**

Proyecto académico realizado para la asignatura **Inteligencia
Artificial y Sistemas Inteligentes**.
