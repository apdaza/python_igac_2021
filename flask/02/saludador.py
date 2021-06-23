from flask import Flask
app = Flask(__name__)

@app.route('/')
def principal():
    return "Bienvenido al saludador"

@app.route('/hello')
def hello():
    return "Hola"

@app.route('/hello/<name>')
def hello_name(name):
    return "Hola %s!" % name

@app.route('/hello/<int:multiplicador>')
def multiplicar_saludo(multiplicador):
    return "hola " * multiplicador

@app.route('/hello/<float:deuda>')
def ver_deuda(deuda):
    return "Hola estan pendientes %f" % deuda

if __name__ == '__main__':
    app.run()
