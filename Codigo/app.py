from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':

        tamaño = int(request.form.get('tamaño', 4))
        fila = int(request.form.get('fila', 0))
        columna = int(request.form.get('columna', 0))
        Recorrido = request.form.get('Recorrido')

        print(f"Tamaño: {tamaño}, Fila: {fila}, Columna: {columna}, Recorrido: {Recorrido}")

        if Recorrido == 'abierto':
            pass

        if Recorrido == 'cerrado':
            pass

        return render_template('Tablero.html', tamaño=tamaño, fila=fila, columna=columna)
    return render_template('Entradas.html')

if __name__ == '__main__':
    app.run(debug=True)