from flask import Flask, render_template, request, session
from logica import generar_ruta_caballo 

app = Flask(__name__)
app.secret_key = 'claveultramegahipersecretaquenadieadivinara'

@app.route('/')
def index():
    return render_template('Entradas.html')

@app.route('/generar', methods=['POST'])
def generar():
    tamaño = int(request.form.get('tamaño'))
    fila = int(request.form.get('fila'))
    columna = int(request.form.get('columna'))
    Recorrido = request.form.get('Recorrido')

    session['tamaño'] = tamaño
    session['fila'] = fila
    session['columna'] = columna
    session['Recorrido'] = Recorrido

    print(f"Tamaño: {tamaño}, Fila: {fila}, Columna: {columna}, Recorrido: {Recorrido}")

    tipo = Recorrido
    Ruta = generar_ruta_caballo(tamaño, fila, columna, tipo) or []
    
    return render_template('Ruta.html', Ruta=Ruta, Tamaño=tamaño, Tipo=tipo)

@app.route('/reiniciar')
def reiniciar():
    tamaño = session.get('tamaño')
    fila = session.get('fila')
    columna = session.get('columna')
    Recorrido = session.get('Recorrido')
    
    tipo = Recorrido
    Ruta = generar_ruta_caballo(tamaño, fila, columna, tipo) or []
    
    return render_template('Ruta.html', Ruta=Ruta, Tamaño=tamaño, Tipo=tipo)

if __name__ == '__main__':
    app.run(debug=True)