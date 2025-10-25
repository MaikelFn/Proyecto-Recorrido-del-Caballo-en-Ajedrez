# **♞ Proyecto: Recorrido del Caballo en Ajedrez (Knight’s Tour)**
Repositorio del primer proyecto 

## 🎯 Descripción general

Este proyecto resuelve el problema clásico del Recorrido del Caballo en ajedrez utilizando la técnica de **backtracking**. Permite visualizar el proceso de búsqueda y solución en una interfaz web desarrollada con **Python + Flask**.

---
## 🧠 Tecnologías utilizadas

- Python 3.13
- Flask
- HTML5, CSS3, JavaScript
- Jinja2
---
## 🧰 Estructura del proyecto

```
Codigo/
│
├── app.py                # Servidor Flask y rutas principales
├── logica.py             # Algoritmo y funciones de backtracking
├── static/
│   └── css/
│       └── styles.css    # Estilos de la interfaz
├── templates/
│   ├── Entradas.html     # Formulario de entrada
│   ├── Tablero.html      # Vista previa del tablero
│   ├── Ruta.html         # Animación y resultado
│   ├── Error.html        # Mensajes de error
│   └── macros.jinja2     # Macros reutilizables
│
Documentación/
│
├── DocumentaciónProyecto1.pdf   # Documentación externa
```
---

## Ejecución local

```bash
# 1️⃣ Clonar el repositorio
git clone https://github.com/MaikelFn/Proyecto-Recorrido-del-Caballo-en-Ajedrez.git
cd Proyecto-Recorrido-del-Caballo-en-Ajedrez/Codigo

# 2️⃣ Entrar al directorio
cd Proyecto-Recorrido-del-Caballo-en-Ajedrez

# 3️⃣ Instalar dependencias
pip install flask

# 4️⃣ Ejecutar la aplicación
python app.py
```
**Abrir el navegador y entrar a:**
```
http://127.0.0.1:5000/
```
---
# 🧑‍💻 Autores y créditos

### - **Flores Navarro Maikel Andres**
### - **Wynta Rodriguez Tayler Yadir**
### - **Lopez Cruz Axel Josue**

### Curso: IC-3002 Análisis de Algoritmos  
### Profesor: Ing. Joss Pecou Johnson  
### Escuela de Ingeniería en Computación
---

# 🧾 Bitácora del Proyecto

| **Autor** | **Fecha** | **Cambios realizados** |
|------------|------------|-------------------------|
| **Maikel** | 25/09/2025 | • Creación del repositorio. <br>• Inicialización del entorno virtual. <br>• Creación de los directorios `templates`, `static` y de los archivos `app.py`, `logica.py`, `Entradas.html`, `Tablero.html`. |
| **Maikel** | 27/09/2025 | • Implementación de una interfaz temporal y pruebas con macros de Jinja. <br>• Macro definida para crear el tablero y otra para visualizar la solución. <br>• Configuraciones básicas de `style.css` para representar el tablero y el caballo. |
| **Maikel** | 29/09/2025 | • Implementación de la función para generar la matriz. <br>• Funciones de validación de movimiento y búsqueda de rutas (sin implementar). |
| **Maikel** | 30/09/2025 | • Función de validación de movimiento que verifica límites y casillas visitadas. <br>• Funciones para encontrar ruta abierta y ejecutar movimientos. |
| **Tayler** | 02/10/2025 | • Funciones auxiliares para la funcionalidad de camino cerrado. <br>• Implementación del camino cerrado. |
| **Maikel** | 04/10/2025 | • Eliminación del repositorio anterior y creación de uno nuevo con estrategia *Git Flow*. <br>• Migración de commits al nuevo repositorio. <br>• Documentación interna de `logica.py` según el estándar. |
| **Tayler** | 04/10/2025 | • Mejora de la interfaz gráfica. <br>• Incorporación de ícono de caballo y estilos de tablero. |
| **Axel** | 05/10/2025 | • Creación de nueva plantilla para mostrar la matriz paso a paso usando una macro. <br>• Prueba temporal en `logica.py` para renderizar cada paso en tiempo real. <br>• Dificultades al mostrar la ruta en tiempo real solo con Flask (se muestra todo en una página). |
| **Axel** | 08/10/2025 | • Mejora de la visualización del recorrido en pantalla. <br>• Se detecta ineficiencia al pasar matrices grandes a la plantilla HTML. |
| **Maikel** | 09/10/2025 | • Optimización del paso de datos a la plantilla HTML (ahora solo lista con fila, columna y tipo de movimiento). <br>• Implementación de script para mostrar los pasos y contador en pantalla. <br>• Marcado de colores (verde: avance, rojo: retroceso) y numeración de pasos. <br>**Pendientes:** <br> a. Fusionar parte gráfica de `logica.py` con `app.py`. <br> b. Documentación interna (HTML, CSS, `app.py`). <br> c. Actualizar Ruta Cerrada para registrar pasos y habilitar botones. <br> d. Agregar estadísticas. <br> e. Documentación externa. |
| **Axel** | 09/10/2025 | • Importación de funciones de `logica.py` y migración de renderizado al `app.py`. <br>• Creación de función para generar cada tipo de ruta. <br>• Se añade el array de movimientos en el camino cerrado. |
| **Tayler** | 11/10/2025 | • Botón de inicio. <br>• Botón de reinicio. <br>• Botón “ver final”. <br>• Integración de la matriz final en la lista de ruta. <br>• Configuración de manejo de sesión. |
| **Axel** | 13/10/2025 | • Se modifica la función de generación de ruta para contar el tiempo de ejecución. <br>• Se añade el tiempo de ejecución en la interfaz. |
| **Axel** | 13/10/2025 | • Se mejora la interfaz para mostrar mensajes cuando no se encuentre una ruta válida. <br>• Cambios visuales en CSS. <br>• Mejoras de usabilidad en botones. |
| **Axel** | 17/10/2025 | • Comentarios explicativos en HTML (documentación externa). <br>• Comentarios de entradas, salidas y restricciones en `app.py`. |
| **Tayler** | 18/10/2025 | • Creación de plantilla HTML para errores. <br>• Modificación de rutas para manejar errores fuera de la vista principal. <br>• Validaciones para tamaño del tablero y existencia de ruta. <br>• Script para evitar rutas cerradas en tableros impares. |
| **Maikel** | 18/10/2025 | • Restricción de entradas con decimales. <br>• Reemplazo de inputs por selects para evitar errores. <br>• Nuevos estilos para entradas. |
| **Maikel** | 23/10/2025 | • Comentarios adicionales en HTML. <br>• Cambio de valor por defecto del formulario (7x7, posición 0,0). <br>• Actualización de comentarios en `app.py` y `logica.py`. <br>• Eliminación del entorno virtual. <br>• Contador de retrocesos y mejora en la función de “ver tablero final”. <br>• Agregada la información del proyecto al `README.md`. |
| **Tayler y Axel** | 23/10/2025 | • Ajustes finales y revisión conjunta del código. |
| **Tayler** | 24/10/2025 | • Limpieza y reestructuración de código en `logica.py`. |
| **Tayler, Maikel y Axel** | 24/10/2025 | • Verificación y arreglos en la documentación externa. <br>• Actualización de la bitácora con commits finales del proyecto. |
| **Tayler** | 24/10/2025 | • Documentación externa final subida al repositorio. |
| **Tayler** | 24/10/2025 | • Bitácora en el  `READ.ME`. |


---
**Repositorio:**  
[GitHub - Proyecto-Recorrido-del-Caballo-en-Ajedrez](https://github.com/MaikelFn/Proyecto-Recorrido-del-Caballo-en-Ajedrez)
