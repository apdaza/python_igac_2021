from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hola Mundo"

@app.route('/flask')
def hello_flask():
    return "Hola Mundo en flask"

if __name__ == "__main__":
    app.run()
