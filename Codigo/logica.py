"""
Módulo de lógica para el Recorrido del Caballo en Ajedrez.

Descripción: Lógica para encontrar un camino válido para el caballo en un tablero de ajedrez.

Autores: Flores Navarro Maikel Andres, Wynta Rodriguez Tayler Yadir, Lopez Cruz Axel Josue.
Fecha: 04-10-2025
"""
import copy
import time
from flask import Flask, render_template, request

app = Flask(__name__)

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
        La matriz se inicializa con -1 en todas las posiciones, excepto en la posición inicial del caballo, que se establece en 'C'.
    """
    tablero = []
    for fila in range(Tamaño):
        subLista = []
        for columna in range(Tamaño):
            subLista.append("N")
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
        Acepta posiciones vacías (-1) y retrocesos ('R') como válidas.
    """
    if 0 <= filaActual < Tamaño and 0 <= colActual < Tamaño:
        if tablero[filaActual][colActual] == "N" or tablero[filaActual][colActual] == 'R':
            return True
    return False

def Guardarruta(tablero, Ruta):
    Ruta.append(copy.deepcopy(tablero))
    return Ruta

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
        
    
    Returns:
        bool: True si se encuentra un camino abierto, False en caso contrario.
    
    Notes:
        Un camino abierto es aquel en el que el caballo no necesariamente regresa a la posición inicial.
        
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
        Esta función marca la posición actual del caballo con 'C' (caballo),
        la posición anterior con 'V' (visitada), y si no se encuentra un camino válido,
        marca con 'R' (retroceso) y retrocede.
        
    """
    tablero[filaAnterior][colAnterior] = 'V'
    tablero[filaActual][colActual] = 'C'
    Guardarruta(tablero, Ruta)
    
    if Encontrar_Camino_Abierto(filaActual, colActual, tablero, Tamaño, contador + 1, Ruta):
        return True

    tablero[filaActual][colActual] = 'R'
    tablero[filaAnterior][colAnterior] = 'C'
    Guardarruta(tablero, Ruta)
    
    return False

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
        if (filaActual, colActual) in soluciones:
            return True
        return False
    
    if Movimiento_Valido(tablero, filaActual+2, colActual-1, Tamaño):
        if Realizar_Movimiento_Cerrado(tablero, filaActual+2, colActual-1, Tamaño, contador, soluciones, filaActual, colActual):
            return True
        
    if Movimiento_Valido(tablero, filaActual+2, colActual+1, Tamaño):
        if Realizar_Movimiento_Cerrado(tablero, filaActual+2, colActual+1, Tamaño, contador, soluciones, filaActual, colActual):
            return True
        
    if Movimiento_Valido(tablero, filaActual-2, colActual-1, Tamaño):
        if Realizar_Movimiento_Cerrado(tablero, filaActual-2, colActual-1, Tamaño, contador, soluciones, filaActual, colActual):
            return True
        
    if Movimiento_Valido(tablero, filaActual-2, colActual+1, Tamaño):
        if Realizar_Movimiento_Cerrado(tablero, filaActual-2, colActual+1, Tamaño, contador, soluciones, filaActual, colActual):
            return True
        
    if Movimiento_Valido(tablero, filaActual+1, colActual-2, Tamaño):
        if Realizar_Movimiento_Cerrado(tablero, filaActual+1, colActual-2, Tamaño, contador, soluciones, filaActual, colActual):
            return True
        
    if Movimiento_Valido(tablero, filaActual-1, colActual-2, Tamaño):
        if Realizar_Movimiento_Cerrado(tablero, filaActual-1, colActual-2, Tamaño, contador, soluciones, filaActual, colActual):
            return True
        
    if Movimiento_Valido(tablero, filaActual+1, colActual+2, Tamaño):
        if Realizar_Movimiento_Cerrado(tablero, filaActual+1, colActual+2, Tamaño, contador, soluciones, filaActual, colActual):
            return True
        
    if Movimiento_Valido(tablero, filaActual-1, colActual+2, Tamaño):
        if Realizar_Movimiento_Cerrado(tablero, filaActual-1, colActual+2, Tamaño, contador, soluciones, filaActual, colActual):
            return True
    return False

def Realizar_Movimiento_Cerrado(tablero, filaActual, colActual, Tamaño, contador, soluciones, filaAnterior, colAnterior):
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
        Esta función marca la posición actual del caballo con 'C' (caballo),
        la posición anterior con 'V' (visitada), y si no se encuentra un camino válido,
        marca con 'R' (retroceso) y retrocede.
        
    """
    tablero[filaActual][colActual] = 'C'
    tablero[filaAnterior][colAnterior] = 'V'
    
    if Encontrar_Camino_Cerrado(filaActual, colActual, tablero, Tamaño, contador + 1, soluciones):
        return True
    tablero[filaActual][colActual] = 'R'
    tablero[filaAnterior][colAnterior] = 'C'
    
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

def PruebaDeRuta():
    tablero2 = CrearTablero(5, 0, 0)

    Ruta=[]
    Guardarruta(tablero2, Ruta)
    if Encontrar_Camino_Abierto(0, 0, tablero2, 5, 1, Ruta):
        return Ruta
    else:
        return None

@app.route('/')
def main():
    Rutas = PruebaDeRuta()
    return render_template('Ruta.html', Rutas=Rutas)
    
    
if __name__ == '__main__':
    app.run(debug=True)
    
