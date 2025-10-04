###########################################################################
#####################  Funciones Generales  ###############################
###########################################################################


# Función para crear el tablero
def CrearTablero(Tamaño, FilaInicial, ColumnaInicial):
    tablero = []
    for fila in range(Tamaño):
        subLista = []
        for columna in range(Tamaño):
            subLista.append(-1)
        tablero.append(subLista)
    tablero[FilaInicial][ColumnaInicial] = 0
    return tablero

#Función para verificar si el movimiento es válido
def Movimiento_Valido(tablero, filaActual, colActual, Tamaño):
    if 0 <= filaActual < Tamaño and 0 <= colActual < Tamaño:
        if tablero[filaActual][colActual] == -1:
            return True
    return False



###########################################################################
########################  Camino Abierto  #################################
###########################################################################

# Función recursiva para encontrar el camino del caballo
def Encontrar_Camino_Abierto(filaActual, colActual, tablero, Tamaño, contador):
    if contador == Tamaño * Tamaño:
        print("Camino Abierto:")
        for linea in tablero:
            print(linea)
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
    tablero[filaActual][colActual] = contador
    print("Matriz Actual:")
    for linea in tablero:
        print(linea)
    if Encontrar_Camino_Abierto(filaActual, colActual, tablero, Tamaño, contador + 1):
        return True
    tablero[filaActual][colActual] = -1
    return False

tablero = CrearTablero(6, 0, 0)
Encontrar_Camino_Abierto(0, 0, tablero, 6, 1)