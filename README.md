# Torre-alfil-y-rey
La pequeña Petya está aprendiendo a jugar al ajedrez. Ya ha aprendido a mover un rey, una torre y un alfil. Permítanos recordarle las reglas para mover piezas de ajedrez. Un tablero de ajedrez son 64 campos cuadrados organizados en una mesa de 8 × 8 . Un campo está representado por un par de números enteros ( r ,  c ) : el número de la fila y el número de la columna (en un juego clásico, las columnas se indexan tradicionalmente con letras). Cada pieza de ajedrez ocupa exactamente un campo. Hacer un movimiento es mover una pieza de ajedrez, las piezas se mueven según las siguientes reglas:  Una torre mueve cualquier número de campos horizontal o verticalmente. Un alfil mueve cualquier número de campos en diagonal. Un rey mueve un campo en cualquier dirección: horizontal, vertical o diagonalmente. Las piezas se mueven así Petya está pensando en el siguiente problema: ¿qué número mínimo de movimientos se necesitan para que cada una de estas piezas se mueva del campo ( r 1 ,  c 1 ) al campo ( r 2 ,  c 2 ) ? En eso, asumimos que no hay más piezas además de esta en el tablero. Ayúdalo a resolver este problema.  Aporte La entrada contiene cuatro números enteros r 1 ,  c 1 ,  r 2 ,  c 2 ( 1 ≤  r 1 ,  c 1 ,  r 2 ,  c 2  ≤ 8 ) - las coordenadas del campo inicial y final. El campo de salida no coincide con el final.  Puede suponer que las filas del tablero de ajedrez están numeradas de arriba a abajo del 1 al 8, y las columnas están numeradas de izquierda a derecha del 1 al 8.  Producción Imprime tres enteros separados por espacios: se necesita el número mínimo de movimientos de la torre, el alfil y el rey (en este orden) para pasar del campo ( r 1 ,  c 1 ) al campo ( r 2 ,  c 2 ) . Si una pieza no puede hacer tal movimiento, imprima un 0 en lugar del número correspondiente.
