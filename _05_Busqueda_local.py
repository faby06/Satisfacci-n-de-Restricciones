import random

# Función para calcular el número de conflictos en el tablero
def calcular_conflictos(tablero):
    n = len(tablero)
    conflictos = 0
    for i in range(n):
        for j in range(i + 1, n):
            # Verifica conflictos en la misma fila o diagonales
            if tablero[i] == tablero[j] or abs(tablero[i] - tablero[j]) == j - i:
                conflictos += 1
    return conflictos

# Función para encontrar una solución utilizando mínimos conflictos
def encontrar_minimos_conflictos(n, max_iter):
    # Inicializa un tablero aleatorio
    tablero = [random.randint(0, n-1) for _ in range(n)]
    
    # Realiza un número máximo de iteraciones
    for _ in range(max_iter):
        conflictos = calcular_conflictos(tablero)
        
        # Si no hay conflictos, hemos encontrado una solución
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
                    
                    # Actualiza la mejor opción si encontramos un mínimo conflicto
                    if nuevos_conflictos < conflicto_min:
                        mejores_movimientos = [fila]
                        conflicto_min = nuevos_conflictos
                    # Si encontramos otro movimiento con el mismo conflicto mínimo, agrégalo
                    elif nuevos_conflictos == conflicto_min:
                        mejores_movimientos.append(fila)
            
            # Elige aleatoriamente uno de los mejores movimientos para la columna actual
            tablero[col] = random.choice(mejores_movimientos)
    
    # Si no encontramos una solución en el número máximo de iteraciones, regresamos None
    return None

n = 8  # Número de reinas
max_iter = 1000  # Máximo de iteraciones

# Intenta encontrar una solución
solucion = encontrar_minimos_conflictos(n, max_iter)

# Imprime el resultado
if solucion is not None:
    print("Solucion encontrada:", solucion)
else:
    print("No se encontro solucion en el numero maximo de iteraciones")

