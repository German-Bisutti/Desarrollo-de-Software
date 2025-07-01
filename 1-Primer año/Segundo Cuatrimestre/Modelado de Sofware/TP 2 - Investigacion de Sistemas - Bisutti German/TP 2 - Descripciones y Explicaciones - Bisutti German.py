"""
1) Relevar y explicar la/las nuevas funcionalidades incluidas en el sistema en la versión 3.1 o 3.2 según corresponda.

El juego en su versión 2.0 tiene una base sólida, la cual se mejora en diferentes aspectos en la versión 3.1. Las partes con cambios en su estructura o agregados son las siguientes:

### Agregados:

En la versión 2.0 se crean tres clases principales: `Arma`, `Jugador` y `Monstruo`. En la versión 3.1, además de conservar estas clases, se incorpora una nueva clase llamada `Cuevas`,
la cual agrega un gran contenido dentro del juego con funcionalidades específicas.

Primero, se define una lista llamada `ListaCuevas`, que contiene descripciones variadas de las cuevas. Estas descripciones son utilizadas luego dentro de la nueva clase `Cuevas` 
para darle más ambientación al entorno del juego.

### Clase `Cuevas`:

Esta clase comienza creando una lista vacía llamada `mundo`, donde se almacenan todas las cuevas generadas a medida que el jugador avanza. Luego define, para cada cueva, sus respectivas coordenadas (`x`, `y`),
conexiones posibles (norte, sur, este, oeste) y rutas habilitadas aleatoriamente entre ellas.

Cada cueva cuenta con:
- Una descripción aleatoria del entorno.
- Una cantidad aleatoria de monedas.
- Un monstruo aleatorio seleccionado de la lista de monstruos.
- Posibles armas en el suelo (con baja probabilidad).

Además, en la clase `Cuevas` se incorporan rutas posibles hacia el norte, sur, este y oeste, que pueden estar habilitadas o no, según una probabilidad definida. 
Cada cueva guarda su propia información, permitiendo que el jugador explore libremente y que los elementos (monstruos, armas, monedas) se mantengan en la cueva aunque el jugador se retire y regrese más tarde.

Este diseño permite generar un mapa dinámico donde cada cueva tiene una posición única en el espacio. Esto representa una mejora significativa respecto a la versión 2.0,
donde el entorno era una única cueva fija.

También se modifica la lógica de la función `avanzar()` para que el jugador pueda elegir una dirección (norte, sur, este u oeste) y desplazarse a una nueva cueva o a una ya explorada.
Se agregan además métodos dentro de la clase `Cuevas` para manejar la interacción con el entorno:

- get_monstruo() → devuelve el monstruo actual de la cueva.
- get_monedas() y `set_monedas()` → permiten acceder y modificar la cantidad de monedas en la cueva.
- lista_armas() → devuelve la lista de armas en el suelo.
- agregar_armas(arma)` → permite dejar un arma en la cueva (por ejemplo, al derrotar un monstruo).

Por último, se agrega la ambientación dinámica mediante descripciones aleatorias de cada cueva, lo cual mejora la inmersión y la narrativa del juego.

Conclusión:

La nueva funcionalidad principal agregada en la versión 3.1 es un sistema de exploración basado en cuevas conectadas, con generación automática de nuevas locaciones,
persistencia de contenido en cada una y ambientación dinámica.


4) Revisar si hay errores de diseño. Explicar posibles soluciones (no es necesario implementarlas).

Convención de nombres: Las clases en Python suelen escribirse con la primera letra en mayúscula. En el código actual se definen como cuevas, arma, jugador y monstruo.
Sería más adecuado escribirlas como Cueva, Arma, Jugador y Monstruo, respetando las convenciones de estilo del lenguaje.

Clase con múltiples responsabilidades: La clase cuevas concentra demasiadas tareas: guarda coordenadas, administra conexiones con otras cuevas, contiene enemigos, armas, monedas, 
y además imprime descripciones. Esto va en contra del principio de responsabilidad única. Sería mejor dividir estas responsabilidades en distintas clases o estructuras.

Código repetido en avanzar(): En el método avanzar se repiten muchos bloques de código similares para cada dirección (norte, sur, este, oeste).
Podría unificarse la lógica para evitar esa repetición.


"""