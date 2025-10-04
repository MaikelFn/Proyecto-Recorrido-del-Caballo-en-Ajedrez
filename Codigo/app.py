from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        tamaño = int(request.form['tamaño'])
        fila = int(request.form['fila'])
        columna = int(request.form['columna'])
        print(f"Tamaño: {tamaño}, Fila: {fila}, Columna: {columna}")
        return render_template('Tablero.html', tamaño=tamaño, fila=fila, columna=columna)
    return render_template('Entradas.html')

if __name__ == '__main__':
    app.run(debug=True)