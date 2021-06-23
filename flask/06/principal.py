from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('carga.html')

@app.route('/uploader', methods = ['POST'])
def cargar():
    if request.method == 'POST':
        archivo = request.files['file']
        archivo.save(secure_filename(archivo.filename))
        lista = [x.split(',') for x in open(secure_filename(archivo.filename)).readlines()]
        return render_template('resultados.html', msg = 'carga exitosa', registros = lista[1:])

if __name__ == "__main__":
    app.run()