from flask import Flask, render_template, request, session
from logica import generar_ruta_caballo 

app = Flask(__name__)
app.secret_key = 'claveultramegahipersecretaquenadieadivinara'

@app.route('/')
def main():
    return render_template('Entradas.html')

@app.route('/tablero', methods=['POST'])
def tablero():
    tamaño = int(request.form.get('tamaño'))
    fila = int(request.form.get('fila'))
    columna = int(request.form.get('columna'))

    session['tamaño'] = tamaño
    session['fila'] = fila
    session['columna'] = columna

    return render_template('Tablero.html', tamaño=tamaño, fila=fila, columna=columna)

@app.route('/generar', methods=['POST'])
def generar():
    tamaño = session.get('tamaño')
    fila = session.get('fila')
    columna = session.get('columna')
    Recorrido = request.form.get('Recorrido')

    session['Recorrido'] = Recorrido

    print(f"Tamaño: {tamaño}, Fila: {fila}, Columna: {columna}, Recorrido: {Recorrido}")

    tipo = Recorrido

    Ruta, tiempo_total = generar_ruta_caballo(tamaño, fila, columna, tipo)
    return render_template('Ruta.html', Ruta=Ruta, Tamaño=tamaño, Tipo=tipo, Tiempo=tiempo_total)


@app.route('/reiniciar')
def reiniciar():
    tamaño = session.get('tamaño')
    fila = session.get('fila')
    columna = session.get('columna')
    Recorrido = session.get('Recorrido')
    
    tipo = Recorrido
    
    Ruta, tiempo_total = generar_ruta_caballo(tamaño, fila, columna, tipo)
    return render_template('Ruta.html', Ruta=Ruta, Tamaño=tamaño, Tipo=tipo, Tiempo=tiempo_total)


@app.route('/inicio')
def inicio():
    session.clear()
    return render_template('Entradas.html')

if __name__ == '__main__':
    app.run(debug=True)