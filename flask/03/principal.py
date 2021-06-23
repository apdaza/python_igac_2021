from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/admin')
def hola_admin():
    return "Hola Admin"

@app.route('/guest/<name>')
def hola_invitado(name):
    return "Hola %s, ingresaste como un invitado" % name

@app.route('/user/<user>')
def principal(user):
    if user == 'admin':
        return redirect(url_for('hola_admin'))
    else:
        return redirect(url_for('hola_invitado', name = user))

if __name__ == '__main__':
    app.run()
                    
