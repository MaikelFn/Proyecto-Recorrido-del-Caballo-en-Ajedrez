# Función para crear el tablero
def CrearTablero(Tamaño, FilaInicial, ColumnaInicial):
    tablero = []
    for fila in range(Tamaño):
        subLista = []
        for columna in range(Tamaño):
            subLista.append(-1)
        tablero.append(subLista)
    tablero[FilaInicial][ColumnaInicial] = 1
    return tablero

# Función recursiva para encontrar el camino del caballo
def Encontrar_Camino(filaActual, colActual, tablero, Tamaño, cont):
    if cont == Tamaño * Tamaño:
        return True
    pass
    
#Función para verificar si el movimiento es válido
def Movimiento_Valido(filaActual, colActual, tablero, Tamaño):
    pass