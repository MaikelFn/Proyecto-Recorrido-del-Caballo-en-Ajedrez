"""
Módulo de lógica para el Recorrido del Caballo en Ajedrez.

Descripción: Lógica para encontrar un camino válido para el caballo en un tablero de ajedrez.

Autores: Flores Navarro Maikel Andres, Wynta Rodriguez Tayler Yadir, Lopez Cruz Axel Josue.
Fecha: 04-10-2025
"""
import copy
import time

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
        La matriz se inicializa con 'N' (no visitada) en todas las posiciones, 
        excepto en la posición inicial del caballo, que se establece en 'C' (caballo).
    """
    tablero = []
    for fila in range(Tamaño):
        subLista = []
        for columna in range(Tamaño):
            subLista.append('N')
        tablero.append(subLista)
    tablero[FilaInicial][ColumnaInicial] = 'C'
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
        Acepta posiciones no visitadas ('N') y retrocesos ('R') como válidas.
    """
    if 0 <= filaActual < Tamaño and 0 <= colActual < Tamaño:
        if tablero[filaActual][colActual] == 'N' or tablero[filaActual][colActual] == 'R':
            return True
    return False


def Encontrar_Camino_Abierto(filaActual, colActual, tablero, Tamaño, contador, Ruta):
    """
    Funcion recursiva para encontrar un camino abierto del caballo en el tablero,
    evaluando todas las posibles posiciones a partir de la posición actual.
    
    Args:
        filaActual (int): Fila actual del caballo.
        colActual (int): Columna actual del caballo.
        tablero (list): Matriz que representa el tablero de ajedrez.
        Tamaño (int): Tamaño del tablero (n x n).
        contador (int): Contador de movimientos realizados por el caballo.
        Ruta (list): Lista que almacena los estados del tablero durante el recorrido.
    
    Returns:
        bool: True si se encuentra un camino abierto, False en caso contrario.
    
    Notes:
        Un camino abierto es aquel en el que el caballo visita todas las casillas del tablero
        pero no necesariamente regresa a la posición inicial.
    """
    if contador == Tamaño * Tamaño:
        return True
    
    if Movimiento_Valido(tablero, filaActual+2, colActual-1, Tamaño):
        if realizar_movimiento_Abierto(tablero, filaActual+2, colActual-1, Tamaño, contador, filaActual, colActual, Ruta):
            return True
        
    if Movimiento_Valido(tablero, filaActual+2, colActual+1, Tamaño):
        if realizar_movimiento_Abierto(tablero, filaActual+2, colActual+1, Tamaño, contador, filaActual, colActual, Ruta):
            return True
        
    if Movimiento_Valido(tablero, filaActual-2, colActual-1, Tamaño):
        if realizar_movimiento_Abierto(tablero, filaActual-2, colActual-1, Tamaño, contador, filaActual, colActual, Ruta):
            return True
        
    if Movimiento_Valido(tablero, filaActual-2, colActual+1, Tamaño):
        if realizar_movimiento_Abierto(tablero, filaActual-2, colActual+1, Tamaño, contador, filaActual, colActual, Ruta):
            return True
        
    if Movimiento_Valido(tablero, filaActual+1, colActual-2, Tamaño):
        if realizar_movimiento_Abierto(tablero, filaActual+1, colActual-2, Tamaño, contador, filaActual, colActual, Ruta):
            return True
        
    if Movimiento_Valido(tablero, filaActual-1, colActual-2, Tamaño):
        if realizar_movimiento_Abierto(tablero, filaActual-1, colActual-2, Tamaño, contador, filaActual, colActual, Ruta):
            return True
        
    if Movimiento_Valido(tablero, filaActual+1, colActual+2, Tamaño):
        if realizar_movimiento_Abierto(tablero, filaActual+1, colActual+2, Tamaño, contador, filaActual, colActual, Ruta):
            return True
        
    if Movimiento_Valido(tablero, filaActual-1, colActual+2, Tamaño):
        if realizar_movimiento_Abierto(tablero, filaActual-1, colActual+2, Tamaño, contador, filaActual, colActual, Ruta):
            return True
        

def realizar_movimiento_Abierto(tablero, filaActual, colActual, Tamaño, contador, filaAnterior, colAnterior, Ruta):
    """
    Realiza el movimiento del caballo en el tablero y guarda la coordenada (filaActual, colActual).
    
    Args:
        Ruta: Lista que almacena tuplas (fila, columna, tipo) donde tipo es 'A' (avance) o 'R' (retroceso)
    """
    tablero[filaAnterior][colAnterior] = 'V'
    tablero[filaActual][colActual] = 'C'
    Ruta.append((filaActual, colActual, 'A'))  # guardar avance
    
    if Encontrar_Camino_Abierto(filaActual, colActual, tablero, Tamaño, contador + 1, Ruta):
        return True

    tablero[filaActual][colActual] = 'R'
    tablero[filaAnterior][colAnterior] = 'C'
    Ruta.append((filaAnterior, colAnterior, 'R'))  # guardar retroceso
    
    return False

def Encontrar_Camino_Cerrado(filaActual, colActual, tablero, Tamaño, contador, soluciones, Ruta):
    """
    Encuentra un camino cerrado del caballo en el tablero, asegurando que el último movimiento
    pueda volver a la posición inicial.
    
    Args:
        filaActual (int): Fila actual del caballo.
        colActual (int): Columna actual del caballo.
        tablero (list): Matriz que representa el tablero de ajedrez.
        Tamaño (int): Tamaño del tablero (n x n).
        contador (int): Contador de movimientos realizados por el caballo.
        soluciones (list): Lista de tuplas con las posiciones adyacentes a la posición inicial.
    
    Returns:
        bool: True si se encuentra un camino cerrado, False en caso contrario.
    
    Notes:
        Un camino cerrado es aquel en el que el caballo visita todas las casillas del tablero
        y termina en una posición adyacente a la inicial, desde la cual puede regresar con un movimiento válido.
    """
    
    if contador == Tamaño * Tamaño:
        if (filaActual, colActual) in soluciones:
            return True
        return False
    
    if Movimiento_Valido(tablero, filaActual+2, colActual-1, Tamaño):
        if Realizar_Movimiento_Cerrado(tablero, filaActual+2, colActual-1, Tamaño, contador, soluciones, filaActual, colActual, Ruta):
            return True
        
    if Movimiento_Valido(tablero, filaActual+2, colActual+1, Tamaño):
        if Realizar_Movimiento_Cerrado(tablero, filaActual+2, colActual+1, Tamaño, contador, soluciones, filaActual, colActual, Ruta):
            return True
        
    if Movimiento_Valido(tablero, filaActual-2, colActual-1, Tamaño):
        if Realizar_Movimiento_Cerrado(tablero, filaActual-2, colActual-1, Tamaño, contador, soluciones, filaActual, colActual, Ruta):
            return True
        
    if Movimiento_Valido(tablero, filaActual-2, colActual+1, Tamaño):
        if Realizar_Movimiento_Cerrado(tablero, filaActual-2, colActual+1, Tamaño, contador, soluciones, filaActual, colActual, Ruta):
            return True
        
    if Movimiento_Valido(tablero, filaActual+1, colActual-2, Tamaño):
        if Realizar_Movimiento_Cerrado(tablero, filaActual+1, colActual-2, Tamaño, contador, soluciones, filaActual, colActual, Ruta):
            return True
        
    if Movimiento_Valido(tablero, filaActual-1, colActual-2, Tamaño):
        if Realizar_Movimiento_Cerrado(tablero, filaActual-1, colActual-2, Tamaño, contador, soluciones, filaActual, colActual, Ruta):
            return True
        
    if Movimiento_Valido(tablero, filaActual+1, colActual+2, Tamaño):
        if Realizar_Movimiento_Cerrado(tablero, filaActual+1, colActual+2, Tamaño, contador, soluciones, filaActual, colActual, Ruta):
            return True
        
    if Movimiento_Valido(tablero, filaActual-1, colActual+2, Tamaño):
        if Realizar_Movimiento_Cerrado(tablero, filaActual-1, colActual+2, Tamaño, contador, soluciones, filaActual, colActual, Ruta):
            return True
    return False

def Realizar_Movimiento_Cerrado(tablero, filaActual, colActual, Tamaño, contador, soluciones, filaAnterior, colAnterior, Ruta):
    """
    Realiza el movimiento del caballo en el tablero y llama recursivamente a la función para continuar el recorrido cerrado.
    
    Args:
        tablero (list): Matriz que representa el tablero de ajedrez.
        filaActual (int): Fila a la que se mueve el caballo.
        colActual (int): Columna a la que se mueve el caballo.
        Tamaño (int): Tamaño del tablero (n x n).
        contador (int): Contador de movimientos realizados por el caballo.
        soluciones (list): Lista de tuplas con las posiciones adyacentes a la posición inicial.
        filaAnterior (int): Fila de la posición anterior del caballo.
        colAnterior (int): Columna de la posición anterior del caballo.
    
    Returns:
        bool: True si se encuentra un camino cerrado, False en caso contrario.
    
    Notes:
        Esta función marca la posición actual del caballo con 'C' (caballo),
        la posición anterior con 'V' (visitada), y si no se encuentra un camino válido,
        marca la posición actual con 'R' (retroceso) y restaura el caballo a la posición anterior.
    """
    tablero[filaAnterior][colAnterior] = 'V'
    tablero[filaActual][colActual] = 'C'
    Ruta.append((filaActual, colActual, 'A'))
    
    if Encontrar_Camino_Cerrado(filaActual, colActual, tablero, Tamaño, contador + 1, soluciones, Ruta):
        return True
    tablero[filaActual][colActual] = 'R'
    tablero[filaAnterior][colAnterior] = 'C'
    Ruta.append((filaAnterior, colAnterior, 'R'))
    
    return False


def Encontrar_Soluciones(tablero, fila, columna, tamaño):
    """
    Encuentra todas las posiciones válidas adyacentes a la posición inicial del caballo.
    
    Args:
        tablero (list): Matriz que representa el tablero de ajedrez.
        fila (int): Fila inicial del caballo.
        columna (int): Columna inicial del caballo.
        tamaño (int): Tamaño del tablero (n x n).
        
    Returns:
        list: Lista de tuplas con las posiciones adyacentes válidas a la posición inicial.
    
    Notes:
        Esta función evalúa los 8 movimientos posibles del caballo desde la posición inicial
        y retorna aquellas posiciones que son válidas (dentro del tablero y no visitadas).
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

def generar_ruta_caballo (tamaño, fila, columna, tipo):
    tablero2 = CrearTablero(tamaño, fila, columna)

    Ruta = [(fila, columna, 'A')]

    if tipo == 'cerrado':
        soluciones = Encontrar_Soluciones(tablero2, fila, columna, tamaño)
        if Encontrar_Camino_Cerrado(fila, columna, tablero2, tamaño, 1, soluciones, Ruta):
            return Ruta
    else:
        if Encontrar_Camino_Abierto(fila, columna, tablero2, tamaño, 1, Ruta):
            return Ruta
    return []

