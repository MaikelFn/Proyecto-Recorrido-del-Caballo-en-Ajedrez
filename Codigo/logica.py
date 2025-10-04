"""
Módulo de lógica para el Recorrido del Caballo en Ajedrez.

Descripción: Lógica para encontrar un camino válido para el caballo en un tablero de ajedrez.

Autores: Flores Navarro Maikel Andres, Wynta Rodriguez Tayler Yadir, Lopez Cruz Axel Josue.
Fecha: 04-10-2025
"""


###########################################################################
#####################  Funciones Generales  ###############################
###########################################################################


def CrearTablero(Tamaño, FilaInicial, ColumnaInicial):
    """
    Funcion encargada de crear la matriz que representa el tablero de ajedrez.
    
    Args:
        Tamaño (int): Tamaño del tablero (n x n).
        FilaInicial (int): Fila inicial del caballo.
        ColumnaInicial (int): Columna inicial del caballo.
        
    Returns:
        list: Matriz que representa el tablero de ajedrez.
    Notes:
        La matriz se inicializa con -1 en todas las posiciones, excepto en la posición inicial del caballo, que se establece en 0.
    """
    tablero = []
    for fila in range(Tamaño):
        subLista = []
        for columna in range(Tamaño):
            subLista.append(-1)
        tablero.append(subLista)
    tablero[FilaInicial][ColumnaInicial] = 0
    return tablero

def Movimiento_Valido(tablero, filaActual, colActual, Tamaño):
    """
    Evalúa si un movimiento esta dentro de los límites del tablero y si la posición no ha sido visitada.
    
    Args:
        tablero (list): Matriz que representa el tablero de ajedrez.
        filaActual (int): Fila actual del caballo.
        colActual (int): Columna actual del caballo.
        Tamaño (int): Tamaño del tablero (n x n).
        
    Returns:
        bool: True si el movimiento es válido, False en caso contrario.
    
    Notes:
        Esta función se utiliza para verificar si el caballo puede moverse a una posición en el tablero.
    """
    if 0 <= filaActual < Tamaño and 0 <= colActual < Tamaño:
        if tablero[filaActual][colActual] == -1:
            return True
    return False



###########################################################################
########################  Camino Abierto  #################################
###########################################################################


def Encontrar_Camino_Abierto(filaActual, colActual, tablero, Tamaño, contador):
    """
    Funcion recursiva para encontrar un camino abierto del caballo en el tablero,
    evaluando todas las posibles posiciones a partir de la posición actual.
    
    Args:
        filaActual (int): Fila actual del caballo.
        colActual (int): Columna actual del caballo.
        tablero (list): Matriz que representa el tablero de ajedrez.
        Tamaño (int): Tamaño del tablero (n x n).
        contador (int): Contador de movimientos realizados por el caballo.
        
    
    Returns:
        bool: True si se encuentra un camino abierto, False en caso contrario.
    
    Notes:
        Un camino abierto es aquel en el que el caballo no necesariamente regresa a la posición inicial.
        
    """
    if contador == Tamaño * Tamaño:
        """print("Camino Abierto:")
        for linea in tablero:
            print(linea)"""
        return True
    
    # L Abajo Izquierda: Fila +2, Columna -1
    if Movimiento_Valido(tablero, filaActual+2, colActual-1, Tamaño):
        if realizar_movimiento_Abierto(tablero, filaActual+2, colActual-1, Tamaño, contador):
            return True
        
    # L Abajo Derecha: Fila +2, Columna +1
    if Movimiento_Valido(tablero, filaActual+2, colActual+1, Tamaño):
        if realizar_movimiento_Abierto(tablero, filaActual+2, colActual+1, Tamaño, contador):
            return True
        
    # L Arriba Izquierda: Fila -2, Columna -1
    if Movimiento_Valido(tablero, filaActual-2, colActual-1, Tamaño):
        if realizar_movimiento_Abierto(tablero, filaActual-2, colActual-1, Tamaño, contador):
            return True
        
    # L Arriba Derecha: Fila -2, Columna +1
    if Movimiento_Valido(tablero, filaActual-2, colActual+1, Tamaño):
        if realizar_movimiento_Abierto(tablero, filaActual-2, colActual+1, Tamaño, contador):
            return True
        
    # L Izquierda Abajo: Fila +1, Columna -2
    if Movimiento_Valido(tablero, filaActual+1, colActual-2, Tamaño):
        if realizar_movimiento_Abierto(tablero, filaActual+1, colActual-2, Tamaño, contador):
            return True
        
    # L Izquierda Arriba: Fila -1, Columna -2
    if Movimiento_Valido(tablero, filaActual-1, colActual-2, Tamaño):
        if realizar_movimiento_Abierto(tablero, filaActual-1, colActual-2, Tamaño, contador):
            return True
        
    # L Derecha Abajo: Fila +1, Columna +2
    if Movimiento_Valido(tablero, filaActual+1, colActual+2, Tamaño):
        if realizar_movimiento_Abierto(tablero, filaActual+1, colActual+2, Tamaño, contador):
            return True
        
    # L Derecha Arriba: Fila -1, Columna +2
    if Movimiento_Valido(tablero, filaActual-1, colActual+2, Tamaño):
        if realizar_movimiento_Abierto(tablero, filaActual-1, colActual+2, Tamaño, contador):
            return True
        

def realizar_movimiento_Abierto(tablero, filaActual, colActual, Tamaño, contador):
    """
    Realiza el movimiento del caballo en el tablero y llama recursivamente a la función para continuar el recorrido.
    
    Args:
        tablero (list): Matriz que representa el tablero de ajedrez.
        filaActual (int): Fila actual del caballo.
        colActual (int): Columna actual del caballo.
        Tamaño (int): Tamaño del tablero (n x n).
        contador (int): Contador de movimientos realizados por el caballo.
        
    
    Returns:
        bool: True si se encuentra un camino, False en caso contrario.
    
    Notes:
        Esta función marca la posición actual del caballo con el contador de movimientos,
        y si no se encuentra un camino válido, desmarca la posición y retrocede.
        
    """
    tablero[filaActual][colActual] = contador
    """print("Matriz Actual:")
    for linea in tablero:
        print(linea)"""
    if Encontrar_Camino_Abierto(filaActual, colActual, tablero, Tamaño, contador + 1):
        return True
    tablero[filaActual][colActual] = -1
    return False


###########################################################################
########################  Camino Cerrado  #################################
###########################################################################


def Encontrar_Camino_Cerrado(filaActual, colActual, tablero, Tamaño, contador, soluciones):
    """
    Encuentra un camino cerrado del caballo en el tablero, asegurando que el último movimiento
    pueda volver a la posición inicial.
    
    Args:
        filaActual (int): Fila actual del caballo.
        colActual (int): Columna actual del caballo.
        tablero (list): Matriz que representa el tablero de ajedrez.
        Tamaño (int): Tamaño del tablero (n x n).
        contador (int): Contador de movimientos realizados por el caballo.
        soluciones (list): Lista de posiciones adyacentes a la posición inicial.        
    
    Returns:
        bool: True si se encuentra un camino cerrado, False en caso contrario.
    
    Notes:
        Un camino cerrado es aquel en el que el caballo puede regresar a la posición inicial
        después de completar todos los movimientos es decir termina en una posición adyacente a la inicial.
        
    """
    
    if contador == Tamaño * Tamaño:
        # Verificar si el último movimiento puede volver al inicio
        if (filaActual, colActual) in soluciones:
            """print("Camino Cerrado:")
            for linea in tablero:
                print(linea)"""
            return True
        return False
    
    # L Abajo Izquierda: Fila +2, Columna -1
    if Movimiento_Valido(tablero, filaActual+2, colActual-1, Tamaño):
        if Realizar_Movimiento_Cerrado(tablero, filaActual+2, colActual-1, Tamaño, contador, soluciones):
            return True
        
    # L Abajo Derecha: Fila +2, Columna +1
    if Movimiento_Valido(tablero, filaActual+2, colActual+1, Tamaño):
        if Realizar_Movimiento_Cerrado(tablero, filaActual+2, colActual+1, Tamaño, contador, soluciones):
            return True
        
    # L Arriba Izquierda: Fila -2, Columna -1
    if Movimiento_Valido(tablero, filaActual-2, colActual-1, Tamaño):
        if Realizar_Movimiento_Cerrado(tablero, filaActual-2, colActual-1, Tamaño, contador, soluciones):
            return True
        
    # L Arriba Derecha: Fila -2, Columna +1
    if Movimiento_Valido(tablero, filaActual-2, colActual+1, Tamaño):
        if Realizar_Movimiento_Cerrado(tablero, filaActual-2, colActual+1, Tamaño, contador, soluciones):
            return True
        
    # L Izquierda Abajo: Fila +1, Columna -2
    if Movimiento_Valido(tablero, filaActual+1, colActual-2, Tamaño):
        if Realizar_Movimiento_Cerrado(tablero, filaActual+1, colActual-2, Tamaño, contador, soluciones):
            return True
        
    # L Izquierda Arriba: Fila -1, Columna -2
    if Movimiento_Valido(tablero, filaActual-1, colActual-2, Tamaño):
        if Realizar_Movimiento_Cerrado(tablero, filaActual-1, colActual-2, Tamaño, contador, soluciones):
            return True
        
    # L Derecha Abajo: Fila +1, Columna +2
    if Movimiento_Valido(tablero, filaActual+1, colActual+2, Tamaño):
        if Realizar_Movimiento_Cerrado(tablero, filaActual+1, colActual+2, Tamaño, contador, soluciones):
            return True
        
    # L Derecha Arriba: Fila -1, Columna +2
    if Movimiento_Valido(tablero, filaActual-1, colActual+2, Tamaño):
        if Realizar_Movimiento_Cerrado(tablero, filaActual-1, colActual+2, Tamaño, contador, soluciones):
            return True
    return False

def Realizar_Movimiento_Cerrado(tablero, filaActual, colActual, Tamaño, contador, soluciones):
    """
    Realiza el movimiento del caballo en el tablero y llama recursivamente a la función para continuar el recorrido.
    
    Args:
        tablero (list): Matriz que representa el tablero de ajedrez.
        filaActual (int): Fila actual del caballo.
        colActual (int): Columna actual del caballo.
        Tamaño (int): Tamaño del tablero (n x n).
        contador (int): Contador de movimientos realizados por el caballo.
        soluciones (list): Lista de posiciones adyacentes a la posición inicial.
        
    Returns:
        bool: True si se encuentra un camino, False en caso contrario.
    
    Notes:
        Esta función marca la posición actual del caballo con el contador de movimientos,
        y si no se encuentra un camino válido, desmarca la posición y retrocede.
        
    """
    tablero[filaActual][colActual] = contador
    if Encontrar_Camino_Cerrado(filaActual, colActual, tablero, Tamaño, contador + 1, soluciones):
        return True
    tablero[filaActual][colActual] = -1
    return False


def Encontrar_Soluciones(tablero, fila, columna, tamaño):
    """
    Encuentra todas las soluciones posibles para el recorrido cerrado del caballo en el tablero(es decir las adyacentes a la posición inicial).
    
    Args:
        tablero (list): Matriz que representa el tablero de ajedrez.
        fila (int): Fila inicial del caballo.
        columna (int): Columna inicial del caballo.
        tamaño (int): Tamaño del tablero (n x n).
        
    Returns:
        list: Lista de tuplas con las posiciones adyacentes a la posición inicial.
    
    Notes:
        Esta función evalúa todas las posibles posiciones a las que el caballo puede moverse desde la posición inicial.
        
    """
    adyacentes = []
    if Movimiento_Valido(tablero, fila + 2, columna - 1, tamaño):
        adyacentes.append((fila + 2, columna - 1))
    if Movimiento_Valido(tablero, fila + 2, columna + 1, tamaño):
        adyacentes.append((fila + 2, columna + 1))
    if Movimiento_Valido(tablero, fila - 2, columna - 1, tamaño):
        adyacentes.append((fila - 2, columna - 1))
    if Movimiento_Valido(tablero, fila - 2, columna + 1, tamaño):
        adyacentes.append((fila - 2, columna + 1))
    if Movimiento_Valido(tablero, fila + 1, columna - 2, tamaño):
        adyacentes.append((fila + 1, columna - 2))
    if Movimiento_Valido(tablero, fila + 1, columna + 2, tamaño):
        adyacentes.append((fila + 1, columna + 2))
    if Movimiento_Valido(tablero, fila - 1, columna - 2, tamaño):
        adyacentes.append((fila - 1, columna - 2))
    if Movimiento_Valido(tablero, fila - 1, columna + 2, tamaño):
        adyacentes.append((fila - 1, columna + 2))
    return adyacentes


###########################################################################
########################  Código de Prueba  ###############################
###########################################################################

tablero = CrearTablero(6, 1, 0)
soluciones = Encontrar_Soluciones(tablero, 1, 0, 6)
tablero2 = CrearTablero(6, 0, 0)


if Encontrar_Camino_Abierto(0, 0, tablero2, 6, 1):
    print("Se encontró un camino abierto:")
    for linea in tablero2:
        print(linea)
else:
    print("No se encontró un camino abierto.")

if Encontrar_Camino_Cerrado(1, 0, tablero, 6, 1, soluciones):
    print("Se encontró un camino cerrado:")
    for linea in tablero:
        print(linea)
else:
    print("No se encontró un camino cerrado.")
