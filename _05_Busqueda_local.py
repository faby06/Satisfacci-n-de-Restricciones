import random

# Funci�n para calcular el n�mero de conflictos en el tablero
def calcular_conflictos(tablero):
    n = len(tablero)
    conflictos = 0
    for i in range(n):
        for j in range(i + 1, n):
            # Verifica conflictos en la misma fila o diagonales
            if tablero[i] == tablero[j] or abs(tablero[i] - tablero[j]) == j - i:
                conflictos += 1
    return conflictos

# Funci�n para encontrar una soluci�n utilizando m�nimos conflictos
def encontrar_minimos_conflictos(n, max_iter):
    # Inicializa un tablero aleatorio
    tablero = [random.randint(0, n-1) for _ in range(n)]
    
    # Realiza un n�mero m�ximo de iteraciones
    for _ in range(max_iter):
        conflictos = calcular_conflictos(tablero)
        
        # Si no hay conflictos, hemos encontrado una soluci�n
        if conflictos == 0:
            return tablero
        
        conflicto_min = float('inf')
        mejores_movimientos = []

        # Para cada columna en el tablero
        for col in range(n):
            actual = tablero[col]
            
            # Prueba diferentes movimientos en esa columna
            for fila in range(n):
                if fila != actual:
                    tablero[col] = fila
                    nuevos_conflictos = calcular_conflictos(tablero)
                    
                    # Actualiza la mejor opci�n si encontramos un m�nimo conflicto
                    if nuevos_conflictos < conflicto_min:
                        mejores_movimientos = [fila]
                        conflicto_min = nuevos_conflictos
                    # Si encontramos otro movimiento con el mismo conflicto m�nimo, agr�galo
                    elif nuevos_conflictos == conflicto_min:
                        mejores_movimientos.append(fila)
            
            # Elige aleatoriamente uno de los mejores movimientos para la columna actual
            tablero[col] = random.choice(mejores_movimientos)
    
    # Si no encontramos una soluci�n en el n�mero m�ximo de iteraciones, regresamos None
    return None

n = 8  # N�mero de reinas
max_iter = 1000  # M�ximo de iteraciones

# Intenta encontrar una soluci�n
solucion = encontrar_minimos_conflictos(n, max_iter)

# Imprime el resultado
if solucion is not None:
    print("Solucion encontrada:", solucion)
else:
    print("No se encontro solucion en el numero maximo de iteraciones")

