# Reto_algoritmos
https://github.com/Diegopj22/Reto_algoritmos.git
## Ejercicio 1
Diseñe un algoritmo que permita calcular cuántos posibles movimientos válidos puede rea- lizar la ficha del caballo, recibiendo como entrada la cantidad de movimientos a realizar desde el inicio, partiendo de todos los números. Por ejemplo, como mostramos anteriormente si la cantidad de movimientos es uno, la cantidad de movimientos válidos son veinte. Pero si la cantidad de mo- vimientos son dos y se sale desde el 1 se puede ir hasta el 6 y el 8 (un movimiento), a continuación, a partir del 6 hasta el 1, 7 y 0 (dos movimientos de la ficha), luego se sigue desde el 8 hasta el 1 y 3 (para alcanzar los dos movimientos de la ficha). En resumen, se tienen cinco posibles movimientos válidos partiendo desde el 1 (1-6-1, 1-6-7, 1-6-0, 1-8-1 y 1-8-3) a estos se deben sumar todos los movi- mientos que resulten de partir de los demás número. En total la cantidad de posibles movimientos válidos para dos movimientos son 46. 

## Ejercicio 2
El caso el problema de las n-reinas, el mismo consiste en ubicar n reinas en un tablero de ajedrez de tamaño n x n, sin que las mismas se amenacen. Recuerde que la reina desplaza de manera hori- zontal, vertical y diagonal como se puede observar en la figura 2, además podemos ver una solución al problema de las 4 reinas. Nótese que una parte importante para resolver un problema es de que manera representar la solución, para este caso particular usamos un vector de n posiciones (colum- nas) y el valor almacenado representa la fila donde se ubica dicha reina.Desarrolle un algoritmo que per- mita hallar al menos una solución para distintas cantidades de reinas
